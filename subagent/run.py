import asyncio

from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

from subagent.main_agent import build_main_agent

async def main():
    model = ChatDeepSeek(model="deepseek-v4-flash")
    agent = build_main_agent(model, 2)
    result = await agent.ainvoke({
        "messages": [
            HumanMessage(content="帮我分析下当前项目下包chapter4下代码")
        ]
    })

    # for i in result['messages']:
    #     msg_type = getattr(result['messages'][i], "type", "?")
    #     print(f'[{i}] {msg_type}: {result['messages'][i].content} \n')
    for i, msg in enumerate(result['messages']):
        msg_type = getattr(msg, "type", "?")
        print(f'整体流程详述：[{i}] {msg_type}: {msg.content} \n')
    print('=================================')
    print("最后答案：：：" + result['messages'][-1].content)
#启动异步函数
asyncio.run(main())