from fastapi import FastAPI
from .tekek import Tekek


app = FastAPI()
logger = Tekek("my_fast_api", app=app)


@app.get("/")
async def root():
    logger.log("root accessed ! hello world!", "root")
    return {"status": "Hello World!"}
