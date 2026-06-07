from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage

from subagent.subagent_config import SubagentConfig


class SubagentExecutor:
    def __init__(self, config: SubagentConfig, model, tools=None):
        self.config = config
        self.model = model
        self.tools = tools or []

    async def run(self, task_prompt: str) -> str:
        print('开始创建子agent，即将开始执行run方法')
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
        for msg in reversed(message):
            if getattr(msg, "type", None) == "ai":
                return str(msg.content)
        return '子agent未返回结果'