from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from middlewares.memory_middleware import MemoryMiddleware

agent = create_agent(
    model="deepseek-v4-flash",
    system_prompt="你是一名小助手",
    middleware=[MemoryMiddleware()],
)

def request_agent(msg: str) -> str:
    result = agent.invoke({
        "messages": [
            HumanMessage(content=msg)
        ]
    })
    res = result['messages'][-1].content
    return res