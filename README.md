<p align=center>
    <img alt="tekek" src="https://raw.githubusercontent.com/dolano-tours/tekek/cddf6ae123a092bed011d065d64a8d01d57d94cc/.rsc/logo_full.svg" width=250/>
</p>

<h1 align=center>Tekek</h1>
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

app = Sanic("REALLY_FAST_API")
logger = Tekek("gotta_go_fast_boi")


@app.route("/", methods=["GET"])
async def root(request):
    logger.log("root accessed ! hello world!", "root")
    return json(
        {
            "status": "Hello World!"
        }
    )


if __name__ == "__main__":
    app.add_task(logger.start())
    app.run(host="0.0.0.0", port=8000)
```

### Fast API



### Your Own Script!

## Da Real Deal!

Go Ahead and Read : <a href="">Usage Documentations</a>