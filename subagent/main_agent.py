from langchain.agents import create_agent

from subagent.task_pool import build_task_tool
from subagent.tools import ALL_TOOLS

# agent = create_agent(
#     model="deepseek-v4-flash",
#     system_prompt="你是一名小助手",
# )
# res = agent.invoke({
#     "message":[{"role":"user", "content":"今天天气怎么样"}]
# })
# print(res)
# print(res['messages'][0].content)

MAIN_AGENT_PROMPT = """
你是主 Agent，负责理解用户问题、拆分复杂任务、汇总最终答案。

你最多只能调用task工具创建{max_subagents}个子agent。
达到上限后，必须基于已有子agent结果进行继续分析，不要再调用task

当任务复杂，并且可以拆成两个或更多相互独立的子任务时，使用 task 工具委托给子 Agent。
适合委托的任务：
- 多文件代码分析
- 多角度调研
- 需要并行探索的问题
- 某个子问题可以独立完成

不要为简单任务调用 task。
不要把一个单步任务包装成子 Agent。

调用 task 前，先做任务分组：
- 如果子任务数量 <= {max_subagents}，可以一个子任务对应一个子 Agent。
- 如果子任务数量 > {max_subagents}，必须把多个子任务合并到同一个子 Agent 的 prompt 中。
- 每个 task 的 prompt 必须列出它负责处理的所有文件/模块/问题。

调用 task 时：
- description 写 3-8 个字的短描述
- prompt 写清楚子 Agent 要完成什么、输出什么
- subagent_type 选择 general-purpose 或 code-reviewer

拿到所有 task 结果后，你需要综合判断，给用户最终答案。
"""

def build_main_agent(model, max_subagent: int):
    task_tool = build_task_tool(
        model=model,
        subagent_tools=ALL_TOOLS,
        max_subagent=max_subagent,
    )
    main_agent_prompt = MAIN_AGENT_PROMPT.format(
        max_subagents=max_subagent,
    )
    return create_agent(
        model=model,
        tools=[task_tool],
        system_prompt=main_agent_prompt,
    )
