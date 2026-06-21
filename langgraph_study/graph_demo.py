import os
from typing import NotRequired, Annotated

from langchain.agents import create_agent, AgentState
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolRuntime


def merge_artifacts(old: list[str] | None, new: list[str] | None) -> list[str]:
    if old is None:
        old = []
    if new is None:
        new = []
    return list(dict.fromkeys(old + new))

#扩展状态
class MyThreadState(AgentState):
    title: NotRequired[str | None]
    artifacts: Annotated[list[str], merge_artifacts]



model = ChatDeepSeek(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

@tool("get_weather")
def get_weather():
    """
    当用户想查询天气时可使用该工具进行查询
    :return: 返回天气
    """
    return '晴天'

@tool()
def remember_name(name: str, runtime: ToolRuntime) -> str:
    user_id = runtime.context.get('user_id', 'default')


check_pointer = InMemorySaver()


agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt='你是一名小助手',
    checkpointer=check_pointer, #用来保存同一个thread_id的历史状态
    state_schema=MyThreadState,
)

config = {
    'configurable': {
        "thread_id": "thread_001"
    }
}

result = agent.invoke(
    {
        "messages": [HumanMessage(content='今天北京天气如何')],
        "title": "学习langgraph",
        "artifacts": ["report.md"],
     },
    config=config,

)

result2 = agent.invoke(
    {
        "messages":[HumanMessage(content='我刚才说了啥')],
        "title": "deep 学习langgraph",
        "artifacts": ["summy.md"],
    },
    config=config
)


# for msg in result['messages']:
#     print(f'type:[{type(msg)}]，消息为：[{msg.content}]')
#
# print('=============')
# for msg in result2['messages']:
#     print(f'type:[{type(msg)}]，消息为：[{msg.content}]')
print(f'result结果为：{result['messages'][-1].content}')
print(f'title为：{result["title"]}')
print(f'artifacts为：{result["artifacts"]}')
#print(f'result2结果为：{result2['messages'][-1].content}')

print('=============')

result2 = agent.invoke(
    {
        "messages":[HumanMessage(content='我刚才说了啥')],
        "title": "deep 学习langgraph",
        "artifacts": ["summy.md"],
    },
    config=config
)


print(f'result2结果为：{result2['messages'][-1].content}')
print(f'title为：{result2["title"]}')
print(f'artifacts为：{result2["artifacts"]}')