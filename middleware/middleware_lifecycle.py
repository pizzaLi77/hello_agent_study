from typing import Any, Callable

from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse, ExtendedModelResponse
from langchain.agents.middleware.types import StateT, ResponseT
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt.tool_node import ToolCallRequest
from langgraph.runtime import Runtime
from langgraph.types import Command
from langgraph.typing import ContextT


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
        print('')

model = ChatDeepSeek(model="deepseek-v4-flash")
agent = create_agent(
    model=model,
    middleware=[MiddlewareLifecycle()],
)
res = agent.invoke({
    "messages": [
        HumanMessage(content="下午好！"),
    ],
})
print(res['messages'][-1].content)