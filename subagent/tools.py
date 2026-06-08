"""
提供给 Agent 使用的文件系统工具集，包括：
- 列出目录
- 读取文件
- 写入文件
- 搜索文件内容
"""

import os
import re
from pathlib import Path

from langchain_core.tools import tool

# 安全工作目录，限制 agent 只能在这个目录下读写
_WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def _resolve_path(file_path: str) -> Path:
    """将相对路径解析为安全的绝对路径，防止目录穿越攻击。"""
    # 如果是绝对路径
    p = Path(file_path)
    if p.is_absolute():
        resolved = p.resolve()
    else:
        resolved = (_WORKSPACE_ROOT / p).resolve()

    # 安全检查：必须在工作目录内
    try:
        resolved.relative_to(_WORKSPACE_ROOT.resolve())
    except ValueError:
        raise ValueError(
            f"路径越界！只允许访问 {_WORKSPACE_ROOT} 目录下的文件。"
            f"请求的路径解析为：{resolved}"
        )
    return resolved


# ========== 读文件 ==========
@tool("read_file")
def read_file(file_path: str, encoding: str = "utf-8", lines: int = 0) -> str:
    """
    读取指定文件的内容。
    :param file_path: 要读取的文件路径（相对于项目根目录）
    :param encoding: 文件编码，默认 utf-8
    :param lines: 只读取前 N 行，0 表示读取全部，默认 0
    :return: 文件内容字符串，含行号标记
    """
    path = _resolve_path(file_path)
    if not path.exists():
        return f"错误：文件不存在 → {file_path}"
    if path.is_dir():
        return f"错误：路径是目录不是文件 → {file_path}"

    try:
        with open(path, encoding=encoding) as f:
            all_lines = f.readlines()
    except UnicodeDecodeError:
        # 尝试用 GBK 编码（Windows 中文环境常见）
        with open(path, encoding="gbk") as f:
            all_lines = f.readlines()

    target = all_lines if lines <= 0 else all_lines[:lines]
    # 加上行号便于引用
    numbered = []
    for i, line in enumerate(target, start=1):
        numbered.append(f"{i:4d}|{line}")
    return "".join(numbered)


# ========== 写文件 ==========
@tool("write_file")
def write_file(file_path: str, content: str, overwrite: bool = False) -> str:
    """
    将内容写入指定文件（默认不覆盖已存在的文件）。
    :param file_path: 要写入的文件路径（相对于项目根目录）
    :param content: 要写入的内容
    :param overwrite: 是否覆盖已有文件，默认 False
    :return: 操作结果描述
    """
    path = _resolve_path(file_path)

    if path.exists() and not overwrite:
        return (
            f"错误：文件已存在，不允许覆盖。"
            f"如确认覆盖请设置 overwrite=True。→ {file_path}"
        )

    # 确保父目录存在
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    size = path.stat().st_size
    return f"写入成功 → {file_path}（{size} 字节）"


# ========== 列出目录 ==========
@tool("list_directory")
def list_directory(dir_path: str = ".") -> str:
    """
    列出指定目录下的所有文件和子目录。
    :param dir_path: 目录路径（相对于项目根目录），默认 "." 表示项目根目录
    :return: 文件和目录列表
    """
    path = _resolve_path(dir_path)
    if not path.exists():
        return f"错误：目录不存在 → {dir_path}"
    if not path.is_dir():
        return f"错误：不是目录 → {dir_path}"

    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
    lines = [f"目录 {path.relative_to(_WORKSPACE_ROOT) or '.'} 的内容："]
    for item in items:
        type_tag = "[DIR] " if item.is_dir() else "[FILE]"
        size = "" if item.is_dir() else f"  ({item.stat().st_size:,} 字节)"
        lines.append(f"  {type_tag} {item.name}{size}")

    total_files = sum(1 for i in items if i.is_file())
    total_dirs = sum(1 for i in items if i.is_dir())
    lines.append(f"\n共 {total_dirs} 个目录，{total_files} 个文件")
    return "\n".join(lines)


# ========== 搜索文件内容 ==========
@tool("search_content")
def search_content(pattern: str, glob: str = "*", dir_path: str = ".") -> str:
    """
    在文件中搜索匹配指定正则模式的内容。
    :param pattern: 要搜索的正则表达式
    :param glob: 文件名过滤，如 "*.py"，默认 "*" 搜索所有文件
    :param dir_path: 搜索的目录路径（相对于项目根目录），默认 "." 表示项目根目录
    :return: 匹配行及其文件位置
    """
    path = _resolve_path(dir_path)
    if not path.exists():
        return f"错误：目录不存在 → {dir_path}"

    results = []
    count = 0
    max_matches = 200  # 防止结果过多

    for file_path in path.rglob(glob):
        if not file_path.is_file():
            continue
        # 跳过虚拟环境和隐藏目录
        try:
            rel = file_path.resolve().relative_to(_WORKSPACE_ROOT.resolve())
        except ValueError:
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue

        try:
            with open(file_path, encoding="utf-8") as f:
                for lineno, line in enumerate(f, 1):
                    if re.search(pattern, line):
                        # 统一用正斜杠
                        display_path = str(rel).replace("\\", "/")
                        results.append(f"{display_path}:{lineno}|{line.rstrip()}")
                        count += 1
                        if count >= max_matches:
                            break
        except (UnicodeDecodeError, PermissionError, OSError):
            continue
        if count >= max_matches:
            break

    if not results:
        return f"未找到匹配 \"{pattern}\" 的内容（目录：{dir_path}，文件过滤：{glob}）"

    header = f'搜索 "{pattern}" 共 {count} 处匹配：\n'
    return header + "\n".join(results)


# ========== 工具集 ==========
# 全部工具列表，可以直接传给 create_agent 的 tools 参数
ALL_TOOLS = [read_file, write_file, list_directory, search_content]

# 只读工具（用于只需要读取分析的场景）
READONLY_TOOLS = [read_file, list_directory, search_content]
