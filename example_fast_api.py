from typing import Optional

import fastapi
from tekek import Tekek


app = fastapi.FastAPI()
logger = Tekek("my_fast_api")



@app.get("/")
async def root():
    logger.log("root accessed ! hello world!", "root")
    return {"status": "Hello World!"}