from fastapi import FastAPI

from fastapi_agent import request_agent
# import logging
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/user/query")
async def root(userid: int, msg: str):
    res = request_agent(msg=msg)
    print(res, flush=True)
    #logger.info(res)
    return {"message": res}