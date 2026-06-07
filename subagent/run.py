import asyncio

from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

from subagent.main_agent import build_main_agent

async def main():
    model = ChatDeepSeek(model="deepseek-v4-flash")
    agent = build_main_agent(model)
    result = await agent.ainvoke({
        "messages": [
            HumanMessage(content="帮我分析下当前项目下包subagent下代码")
        ]
    })
    print(result['messages'][-1].content)

#启动异步函数
asyncio.run(main())