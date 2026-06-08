from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage

from subagent.subagent_config import SubagentConfig


class SubagentExecutor:
    def __init__(self, config: SubagentConfig, model, tools=None):
        self.config = config
        self.model = model
        self.tools = tools or []

    async def run(self, task_prompt: str, seq: int) -> str:
        print(f'第{seq}次创建子agent，即将开始执行run方法')
        print(f'第{seq}个子agent需要做的任务是：{task_prompt}')
        agent = create_agent(
            model=self.model,
            tools=self.tools,
            system_prompt=None,
        )
        state = {
            "messages": [
                SystemMessage(content=self.config.system_prompt),
                HumanMessage(content=task_prompt),
            ]
        }
        result = await agent.ainvoke(state)
        message = result["messages"]
        print(f'第{seq}个子agent返回结果：{message}')
        for msg in reversed(message):
            if getattr(msg, "type", None) == "ai":
                return str(msg.content)
        return '子agent未返回结果'