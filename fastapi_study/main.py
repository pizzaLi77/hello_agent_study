import asyncio
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from fastapi_agent import request_agent
import uvicorn


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    force=True,
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def life_span_test(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info('准备资源life_span_test。。。。')

    async with get_resource() as s:
        logger.info(f'life_span_test方法中拿到get_resource方法资源：{s}')
    yield


    logger.info('释放资源life_span_test。。。。')

@asynccontextmanager
async def get_resource():
    logger.info('即将创建资源server')
    server = '我是资源1'
    yield server
    logger.info('server使用完，即将进行回收')
    logger.info('释放资源server。。')

app = FastAPI(
    lifespan=life_span_test
)

@app.get("/user/query")
async def root(userid: int, msg: str):
    res = request_agent(msg=msg)
    print(res, flush=True)
    #logger.info(res)
    return {"message": res}

if __name__ == '__main__':
    config = uvicorn.Config(
        app,
        host='127.0.0.1',
        port=8000,
        reload=False,
        log_level='debug',)
    server = uvicorn.Server(config)
    asyncio.run(server.serve())