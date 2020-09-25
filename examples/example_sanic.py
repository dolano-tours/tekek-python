from sanic import Sanic
from sanic.response import json
from .tekek import Tekek


app = Sanic("sanic_example")
logger = Tekek("sanic_example", app=app)


@app.route("/", methods=["GET"])
async def root(request):
    logger.log("root accessed ! hello world!", "root")
    return json(
        {
            "status": "Hello World!"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
