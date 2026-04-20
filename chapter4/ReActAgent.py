from datetime import datetime
import re

from chapter4.llm_client import HelloAgentsLLM
from chapter4.tools import ToolExecutor, search

REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手
可用工具如下：
{tools}

请严格按照以下格式进行回应：
Thought: 你的思考过程，用于分析问题、拆解任务和规划下一步行动
Action：你决定采取的行动必须是以下格式之一：
- `{{tool_name}}[{{tool_input}}]`:调用一个可用工具
- `Finish[最终答案]`：当你认为已经获得最终答案时
- 当你收集到足够信息，能够回答用户最终问题时，你必须在`Action:`字段后使用`Finish[最终答案]`  来输出最终答案
现在，请开始解决以下问题：
Question: {question}
History: {history}
"""
class ReActAgent:
    def __init__(self, llm_client: HelloAgentsLLM, tool_executor: ToolExecutor, max_steps: int=5):
        self.llm_client = llm_client
        self.tool_executor = tool_executor
        self.max_steps = max_steps
        self.history = []
    def run(self, question: str):
        """
        运行ReAct智能体来回答一个问题
        """
        self.history = [] #每次运行时重置历史记录
        current_step = 0
        while current_step < self.max_steps:
            current_step += 1
            print(f'-----第{current_step}步--------')
            #格式化提示词
            tools_desc = self.tool_executor.getAvailableTools()
            history_str = '\n'.join(self.history)
            prompt = REACT_PROMPT_TEMPLATE.format(
                tools=tools_desc,
                question=question,
                history=history_str,
            )
            #调用llm进行思考
            messages = [{"role": "user", "content": prompt}]
            response_text = self.llm_client.think(messages=messages)
            if not response_text:
                print("错误：llm未能返回有效响应")
                break

            thought, action = self._parse_output(response_text)
            if thought:
                print(f'思考：{thought}')
            if not action:
                print('警告：未能解析出有效的Action,流程终止。')
                break
            #执行action
            if action.startswith('Finish'):
                #若是Finish开头，表示llm准备输出最终答案
                final_answer = re.match(r"\w+\[(.*)\]", action, re.DOTALL).group(1)
                print(f'🎆 最终答案：{final_answer}')
                return final_answer
            tool_name, tool_input = self._parse_action(action)
            if not tool_name or not tool_input:
                continue
            print(f'🎬 行动：{tool_name}[{tool_input}]')
            tool_function = self.tool_executor.getTool(tool_name)
            if not tool_function:
                observa = f'错误：未找到名为：{tool_name}的工具'
            else:
                observa = tool_function(tool_input) #调用真实工具
            print(f'👀 观察：{observa}')
            #将action本身和工具执行后的observa添加到历史记录中，为下一轮提供新的上下文
            self.history.append(f'Action：{action}')
            self.history.append(f'observa: {observa}')
        print("循环已达最大步数，流程终止")
        return None


    def _parse_output(self, text: str):
        """
        解析LLM的输出，提取Thought和Action
        """
        #Thought 匹配到Action或文本末尾
        thought_match = re.search(r"Thought:\s*(.*?)(?=\nAction:|$)", text, re.DOTALL)
        #Action匹配到文本末尾
        action_match = re.search(r"Action:\s*(.*?)$", text, re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        return thought, action
    def _parse_action(self, action_text: str):
        """
        解析Action字符串，提取工具名称和输入
        """
        match = re.match(r"(\w+)\[(.*)\]", action_text, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return None, None


if __name__ == '__main__':
    llm = HelloAgentsLLM()
    tool_executor = ToolExecutor()
    search_description = "一个网页搜索引擎，当你需要回答关于时事、事实以及在知识库找不到信息时，应用此工具"
    tool_executor.registerTool("Search", search_description, search)
    react_agent = ReActAgent(llm_client=llm, tool_executor=tool_executor)
    question = "苹果在2026年最新手机是哪一款，主要卖点是什么？"
    react_agent.run(question)
