<h1 align=center>Tekek</h1>

<p align=center>
    <img alt="tekek" src="https://raw.githubusercontent.com/dolano-tours/tekek/cddf6ae123a092bed011d065d64a8d01d57d94cc/.rsc/logo_full.svg" width=250/>
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

## Usage

### Install
Tekek is available via **PyPI** you can install it using `pip`

```shell script
python3 -m pip install tekek
```

Import `Tekek` and instantiate.

### Basic Usage

```python
from tekek import Tekek


logger = Tekek(name=__name__)
```

By default, tekek came with 7 levels of log record

```python
logger.log("IDENTIFIER", "MESSAGE")
logger.debug("IDENTIFIER", "MESSAGE")
logger.info("IDENTIFIER", "MESSAGE")
logger.warning("IDENTIFIER", "MESSAGE")
logger.error("IDENTIFIER", "MESSAGE")
logger.exception("IDENTIFIER", "MESSAGE")
logger.critical("IDENTIFIER", "MESSAGE")
```

example basic usage:

```python
def function_a():
    logger.log("function_a", "function a starts !")
    try:
        ...  # Some Algorithm
        logger.info("function_a", "finished doing things")
    except Exception as e:
        logger.exception("function_a", "Exception raised {}".format(e))
    
    logger.debug("function_a", "function a finished !")
    return

def function_b():
    logger.error("function_b", "this error came from function b")
```

### Advanced Usage

Read : <a href="">Documentations</a>