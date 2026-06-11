from typing import Any, Callable

from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse, ExtendedModelResponse
from langchain.agents.middleware.types import StateT, ResponseT
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt.tool_node import ToolCallRequest
from langgraph.runtime import Runtime
from langgraph.types import Command
from langgraph.typing import ContextT

@tool('get_weather')
def get_weather():
    """
    获取天气信息
    :return:
    """
    print('进入到get_weather工具调用。。。')
    return '小雨'

class MiddlewareLifecycle(AgentMiddleware):
    def before_agent(self, state: StateT, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        print('before_agent方法执行。。。')
        return None
    def before_model(self, state: StateT, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        print('before_model方法执行。。。')
        return None
    def after_model(self, state: StateT, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        print('after_model方法执行。。。')
        return None
    def after_agent(self, state: StateT, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        print('after_agent方法执行。。。')
        return None
    def wrap_model_call(
        self,
        request: ModelRequest[ContextT],
        handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
    ) -> ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]:
        print('模型调用前进入方法wrap_model_call。。。')
        response = handler(request)
        print('模型调用后进入方法wrap_model_call。。。')
        return response
    def wrap_tool_call(
        self,
        request: ToolCallRequest,
        handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
    ) -> ToolMessage | Command[Any]:
        print('工具调用前进入方法wrap_tool_call。。')
        response = handler(request)
        print('工具调用后进入方法wrap_tool_call。。')
        return response

model = ChatDeepSeek(model="deepseek-v4-flash")
agent = create_agent(
    model=model,
    middleware=[MiddlewareLifecycle()],
    tools=[get_weather],
    system_prompt='你是一名小助手，回答用户问题'
)
res = agent.invoke({
    "messages": [
        HumanMessage(content="下午好，今天天气怎么样！"),
    ],
})
for msg in res['messages']:
    print(f'类型：{msg.type}，发送消息为：{msg.content}')
#print(res['messages'][-1].content)


if __name__ == '__main__':
    flag1 = True
    flag2 = False
    print(flag1 and flag2)