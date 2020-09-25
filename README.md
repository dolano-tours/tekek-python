<p align=center>
    <img alt="tekek" src="https://raw.githubusercontent.com/dolano-tours/tekek/cddf6ae123a092bed011d065d64a8d01d57d94cc/.rsc/logo_full.svg" width=250/>
</p>

<h1 align=center>Tekek</h1>
<p align=center>
<img alt="Travis (.org)" src="https://img.shields.io/travis/dolano-tours/tekek/nightly?label=nightly-build">
<img alt="Travis (.org)" src="https://img.shields.io/travis/dolano-tours/tekek/production?label=production-build">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/tekek">
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/tekek">
<img alt="PyPI" src="https://img.shields.io/pypi/v/tekek">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/tekek">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/tekek">

<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/tekek">
</p>
<p align=center><b>Tekek</b> [təʔkəʔ] is easy to use, fast, server-agnostic, asynchronous, highly configurable local and remote logging tool </p>

## Features

- Semi-Direct Replacement for python built-in's logger
- Asynchronous
- <sub>Support Websocket <super><i><b>(WIP)</b></i></super></sub>
- Reliable Remote Logging
- Reliable File Logging
- Reliable Console Logging
- Highly Configurable

## Installation
Tekek is available via **PyPI** you can install it using `pip`

```shell script
python3 -m pip install tekek
```

Import `Tekek` and instantiate.

## Hello World

```python
from tekek import Tekek


logger = Tekek(name=__name__)
```

By default, tekek came with 7 levels of log record

```python
logger.log("MESSAGE")
logger.debug("MESSAGE")
logger.info("MESSAGE")
logger.warning("MESSAGE")
logger.error("MESSAGE")
logger.exception("MESSAGE")
logger.critical("MESSAGE")
```

example basic usage:

```python
def function_a():
    logger.log("function a starts !", identifier="function_a")
    try:
        ...  # Some Algorithm
        logger.info("finished doing things", "function_a")
    except Exception as e:
        logger.exception("Exception raised {}".format(e), "function_a")

    logger.debug(identifier="function_a", message="function a finished !")
    return

def function_b():
    logger.error("this error came from function b", "function_a")
```

and yes it is regular function not an `async` function. why ? Because **Tekek** is smart enough to handle it for you. don't worry it barely scratch your application performance

## Compatibility Example

### Sanic

oh yeah, if you _**Gotta Go Fast**_, you need to develop it **FAST** ! use tekek as your logging and debugging tool !

```python
from sanic import Sanic
from sanic.response import json
from tekek import Tekek

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
```

### Fast API

A beautiful API Framework need a beautiful tekek as well ;)

```python
from fastapi import FastAPI
from tekek import Tekek


app = FastAPI()
logger = Tekek("my_fast_api", app=app)


@app.get("/")
async def root():
    logger.log("root accessed ! hello world!", "root")
    return {"status": "Hello World!"}
```

### Your Own Script!

Of course you can use your own app! let's create `my_app` as an example

using `coroutine` function

```python
import asyncio
from tekek import Tekek


logger = Tekek("mah_own")


async def my_app(some_param: int):
    logger.log(f"My App Run Successfully! {some_param}")
    ...  # Your Beautiful app

    return True


async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    await asyncio.gather(
        my_app(3),
        logger.start()
    )


if __name__ == '__main__':
    asyncio.run(main())
```

using `class`

```python
import asyncio
from tekek import Tekek


logger = Tekek("mah_own")


class MyApp:
    def __init__(self):
        self.some_vars = 3

    async def app(self):
        logger.log(f"App Ran! {self.some_vars}")
        ...  # Your beautiful app

    async def start(self):
        asyncio.ensure_future(self.app())


my_app = MyApp()


async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    await asyncio.gather(
        my_app.start(),
        logger.start()
    )


if __name__ == '__main__':
    asyncio.run(main())
```

## Da Real Deal!

Go Ahead and Read : <a href="">Usage Documentations</a>