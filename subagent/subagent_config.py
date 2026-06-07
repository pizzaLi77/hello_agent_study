from dataclasses import dataclass

#@dataclass 是 Python 3.7 引入的装饰器，
#作用就是自动帮你生成 __init__、__repr__、__eq__ 等方法，省去手写样板代码。
@dataclass
class SubagentConfig:
    name: str
    description: str
    system_prompt: str
    model: str = "inherit"
    max_turns: int = 20
    timeout_seconds: int = 300

SUBAGENTS = {
    "general-purpose": SubagentConfig(
        name="general-purpose",
        description="用于复杂分析，代码阅读，多步骤任务",
        system_prompt=(
            "你是一个子 Agent。你只负责完成主 Agent 分配给你的任务。"
            "不要反问用户，信息不足时基于已有上下文给出最佳结果。"
            "完成后返回简洁总结、关键发现和必要证据。"
        ),
    ),
    "code-reviewer": SubagentConfig(
        name="code-reviewer",
        description="专门做代码审查和风险分析",
        system_prompt=(
            "你是代码审查子 Agent。重点找 bug、边界条件、测试缺口和设计风险。"
            "输出按严重程度排序。"
        ),
    ),
}

def get_subagent_config(name :str):
    return SUBAGENTS[name]