from langchain_core.tools import tool

from subagent.subagent_config import get_subagent_config
from subagent.subagent_executor import SubagentExecutor


def build_task_tool(model, subagent_tools=None, max_subagent: int = 3):
    count_num = 0
    @tool("task")
    async def task(description: str, prompt: str, subagent_type: str) -> str:
        """把任务委托给一个子agent执行。
        :param description: 简短任务描述
        :param prompt: 给子agent的完整任务说明
        :param subagent_type: 子agent类型，如general-purpose,code-reviewer
        """
        nonlocal count_num
        if count_num >= max_subagent:
            return '子agent数量已达上限，请主agent基于已有结果总结，不要再去创建子agent'

        count_num += 1
        print(f'第{count_num}次调用task工具方法创建子agent，其中subagent_type为：{subagent_type}')
        print(f'第{count_num}次task工具方法中prompt为：{prompt}，描述为：{description}')
        config = get_subagent_config(subagent_type)
        if config is None:
            return f'未知子agent类型：{subagent_type}'
        executor = SubagentExecutor(
            config=config,
            model=model,
            tools=subagent_tools or [],
        )
        result = await executor.run(prompt, count_num)
        return f'task success:{result}'
    return task