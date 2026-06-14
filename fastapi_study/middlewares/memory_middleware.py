from typing import Any, override

from langchain.agents import AgentState
from langchain.agents.middleware import AgentMiddleware
from langchain.agents.middleware.types import StateT
from langgraph.runtime import Runtime
from langgraph.typing import ContextT

from fastapi_study.queues import MemoryUpdateQueue


class MemoryMiddlewareState(AgentState):
    pass

class MemoryMiddleware(AgentMiddleware[MemoryMiddlewareState]):
    state_schema = MemoryMiddlewareState
    @override
    def after_agent(self, state: MemoryMiddlewareState, runtime: Runtime[ContextT]) -> dict[str, Any] | None:
        #print(f'state为：{state}')
        filtered = []
        for msg in state.get('messages', []):
            if msg.type == 'human':
                #filtered.append('human:'.join(msg.content))
                filtered.append(msg.content)
            elif msg.type == 'ai':
                #filtered.append('ai:'.join(msg.content))
                filtered.append(msg.content)
        # print(state.get('messages')[0].type)
        print(filtered)
        queue = MemoryUpdateQueue()
        queue.add(filtered)
        print('进入到after_agent中间件')