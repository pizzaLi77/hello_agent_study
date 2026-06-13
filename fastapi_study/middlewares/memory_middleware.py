from typing import Any, override

from langchain.agents import AgentState
from langchain.agents.middleware import AgentMiddleware
from langchain.agents.middleware.types import StateT
from langgraph.runtime import Runtime
from langgraph.typing import ContextT

class MemoryMiddlewareState(AgentState):
    pass

class MemoryMiddleware(AgentMiddleware[MemoryMiddlewareState]):
    state_schema = MemoryMiddlewareState
    @override
    def after_agent(self, state: MemoryMiddlewareState, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        print(f'state为：{state}')
        print('进入到after_agent中间件')