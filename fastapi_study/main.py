import asyncio
import logging

from fastapi import FastAPI

from fastapi_agent import request_agent
import uvicorn


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    force=True,
)
logger = logging.getLogger(__name__)

app = FastAPI()

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