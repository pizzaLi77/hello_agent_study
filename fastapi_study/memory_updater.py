import logging
import os
import uuid

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_deepseek import ChatDeepSeek
from openai import api_key, base_url
from openai.types import ChatModel

logger = logging.getLogger(__name__)

MEMORY_PROMPT = """
你是一名持久化记忆小助手,根据最新汇总记忆进行总结然后持久化记忆
"""


class MemoryUpdater:
    def __init__(self):
        pass

    def updateMemory(self, msg):
        logger.info('即将进行持久化记忆。。。')
        print('即将进行持久化记忆。。。。')
        pre_memory_content = ''
        #读取当前记忆
        #加r目的是防止转义
        file_path_main = r'D:\develop\pycharmcode\hello_agent_study\memory_file'
        temp = uuid.uuid4().hex
        full_path_temp = file_path_main + '\\' + temp + '.tmp'
        full_path_main = file_path_main + '\\' + 'memory_01.txt'
        #memory_01.txt
        with open(full_path_main, 'r', encoding='utf-8') as f:
            pre_memory_content = f.read()
        logger.info(f'读取到之前记忆为：{pre_memory_content}')
        new_memory_content = pre_memory_content.join(msg)
        logger.info(f'最新记忆汇总为:{new_memory_content}')
        model = ChatDeepSeek(
            model="deepseek-v4-flash",
            api_key=os.getenv("DEEPSEEK_API_KEY")
        )
        result = model.invoke([
            SystemMessage(content=MEMORY_PROMPT),
            HumanMessage(content=new_memory_content)
        ])

        #先写入临时文件，然后再原子化写入正在路径下文件，防止写一半宕机污染记忆文件
        with open(full_path_temp, 'w', encoding='utf-8') as f:
            f.write(str(result.content))
        #移动并覆盖，临时文件会自动删掉
        os.replace(full_path_temp, full_path_main)
        logger.info("持久化记忆完成。。。")
        return True