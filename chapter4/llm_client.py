import os

from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent.parent / "llm.env")
class HelloAgentsLLM:
    def __init__(self, model: str = None, apiKey: str = None, baseUrl: str = None, timeout: int = None):
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey = apiKey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_HTTP_TIMEOUT", 60))
        if not all([self.model, apiKey, baseUrl]):
            raise ValueError("模型id，api密钥，服务地址需提供或在env文件定义")
        self.client = OpenAI(api_key=apiKey, base_url=baseUrl, timeout=timeout)

    def think(self, messages: list[dict[str, str]], temperature: float = 0.5) -> str:
        print(f"正在调用{self.model}模型🧠。。。")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )
            print("llm model response success。。。")
            collected_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()
            return "".join(collected_content)
        except Exception as e:
            print(f"调用llm api error，error_reason:{e}")
            return None

if __name__ == "__main__":
    try:
        llm_client = HelloAgentsLLM()
        example_message = [
            {"role": "system", "content": "you are a helpful doctor"},
            {"role": "user", "content": "下午好"}
        ]
        print("===llm...===")
        response_text = llm_client.think(example_message)
        # if response_text:
        #     print("--respinse--")
        #     print(response_text)
    except Exception as e:
        print(e)









