<p align=center>
    <img src="https://raw.githubusercontent.com/dolano-tours/tekek/cddf6ae123a092bed011d065d64a8d01d57d94cc/.rsc/logo_plain.svg" width=300>
</p>

<h1 align=center>Usage</h1>

## Advanced Usage

### Console Logging

console logging is enabled by default, but you still have the option to disable it.
to disable console logging by setting `console_logging` to `False`, by default `console_logging` is set to `True`

```python
logger = Tekek(
    name=__name__,
    console_logging=False
)
```

to set which system file to use you can set it using `console_file`. by default `console_file` is set to `stderr`

```python
logger = Tekek(
    name=__name__,
    console_file=sys.stdout
)
```

or you can disable console logging in any point in runtime by calling `disable_console` method

```python
logger.disable_console()
```

and you can re enable it with `enable_console`

```python
logger.enable_console()
```

### File Logging

to enable file logging feature, set `file_logging` to `True`. and set `file_path` to your desired file name / path

```python
logger = Tekek(
    name=__name__,
    file_logging=True,
    file_path="./log/log.txt"
)
```

or you can disable console logging in any point in runtime by calling `disable_file`

```python
logger.disable_file()
```

and you can re enable it with `enable_file`

```python
logger.enable_file()
```

### Remote Logging

to enable remote logging, you just need to set `remote_logging` to `True` and set the remote `remote_path` to your desired server host

```python
logger = Tekek(
    name=__name__,
    remote_logging=True,
    remote_path="https://log.mydomain.com"
)
```

or you can disable console logging in any point in runtime by calling `disable_remote` method

```python
logger.disable_remote()
```

and you can re enable it with `enable_remote`

```python
logger.enable_remote()
```

### Combinations

it's possible to use all of the above features

```python
logger = Tekek(
    name=__name__,
    console_logging=True,                       # Enable Console Logging, it's enabled by default
    console_file=sys.stdout
    remote_logging=True,                        # Enable Remote Logging
    remote_path="https://log.mydomain.com",
    file_logging=True,                          # Enable File Logging
    file_path="./log/log.txt"
)
```

## Customization

### Concept

Every Level is described by LevelModel which define it's `Level` model, `RequestMeta` model, `RequestModel` model.

#### Level

`Level` model are created using `Level` data class with parameter of

- `name`: the name of the level
- `importance`: how important is it ?

Tekek came with :

- log
  - `name` = "LOG"
  - `importance` = 10
- debug
  - `name` = "DEBUG"
  - `importance` = 10
- info
  - `name` = "INFO"
  - `importance` = 20
- warning
  - `name` = "WARNING"
  - `importance` = 30
- error
  - `name` = "ERROR"
  - `importance` = 40
- exception
  - `name` = "EXCEPTION"
  - `importance` = 40  
- critical
  - `name` = "CRITICAL"
  - `importance` = 50

every `Level` are instantiated with:

```python
error_model: Level = Level(name="ERROR", importance=40)
```

#### Request Meta

`RequestMeta` define which _**HTTP Method**_ to use, which _**request body structure**_ to use, what host to send request with.

Tekek default `RequestMeta` structure are :

```python
request_meta: RequestMeta = RequestMeta(
    method_type=MethodType.POST,
    body_type=RequestBodyType.JSON,
    host=...  # <SPECIFIED WHEN TEKEK ARE INSTANTIATED WITH remote_path PARAMETER>
)
```

#### Request Model

`RequestModel` define the request body structure. each parameter means what is the `key` attribute to use for each `Record` attributes. Tekek came with three different type of `RequestModel` which is:

- `RequestModel` it self. the generic type without `Record`'s level attribute

  ```python
  @dataclass
  class RequestModel:
      uuid: str
      timestamp: str
      identifier: str
      message: str
  ```

- `RequestModelJSON` which inherit `RequestModel` with `Record`'s level attribute structured as nested dict described with `LevelRequestModel`

  ```python
  request_model_json: RequestModelJSON = RequestModelJSON(
      uuid="uuid",
      timestamp="timestamp",
      identifier="identifier",
      message="message",
      level=LevelRequestModel(
          root="level",
          name="name",
          importance="importance"
      )
  )
  ```

  the output will be:

  ```json
  {
    "uuid": Record.uuid,
    "timestamp": Record.timestamp,
    "identifier": Record.identifier,
    "message": Record.message,
    "level": {
      "name": Record.level.name,
      "importance": Record.level.importance
    }
  }
  ```

- `RequestModelFORM` which inherit `RequestModel` with `Record`'s level attribute structured as flat dict.

  ```python
  self.request_model_form: RequestModelFORM = RequestModelFORM(
      uuid="uuid",
      timestamp="timestamp",
      identifier="identifier",
      message="message",
      level_name="level_name",
      level_importance="level_importance"
  )
  ```

  which output will be :

  ```json
  {
    "uuid": Record.uuid,
    "timestamp": Record.timestamp,
    "identifier": Record.identifier,
    "message": Record.message,
    "level_name": Record.level.name,
    "level_importance": Record.level.importance
  }
  ```

#### LevelModel Model

Last, after all requirement are met we instantiate the `LevelModel`. take a look of Tekek's default model of `ERROR` as an example

```python
ERROR = LevelModel(
    model=error_model,
    request_meta=request_meta,
    request_model=request_model
)
```

### Add New Level

you can add your own level by using `add_level` method

#### Using Level

by using level, means you are using current set or default `RequestMeta` or `RequestModel` for your current model
```python
from tekek import Tekek
from tekek.models import Level

logger = Tekek(__name__)

my_new_level: Level = Level(        # Create new Level
    name="LEVEL_NAME",              # Name your Level
    importance=5                    # Lower is less important
)
logger.add_level(my_new_level)
```

#### Using LevelModel

level model enable you to directly modify your request meta and/or request model

first create your level
```python
from tekek import Tekek
from tekek.models import LevelModel
from tekek.models import Level, LevelRequestModel, RequestMeta, RequestModel

my_new_level: Level = Level(        # Create new Level
    name="VERY_IMPORTANT",          # Name your Level
    importance=5                    # Lower is less important
)
```

then define the request meta or in other words request configuration

```python
my_new_request_meta: RequestMeta =\
    RequestMeta(
        method_type=MethodType.PUT,                       # Set method type to PUT
        body_type=RequestBodyType.JSON,                   # set request body type as JSON
        host="https://my.customdomain.com/VERY_IMPORTANT" # set your own custom remote host
    )
```

also define the request model, so tekek new how to transpile it into **json** since you just define the body type as `JSON`

```python
my_new_request_model: RequestModelJSON =\
    RequestModelJSON(
        uuid="id",
        timestamp="time",
        identifier="func_name",
        message="msg",
        level=LevelRequestModel(
            root="lvl",
            name="lname",
            importance="limportanity"
        )
    )
```

above specifications will send `PUT` Request to `https://my.customdomain.com/VERY_IMPORTANT` with request body type of `JSON` with structure:

```json
{
  "id": Record.uuid,
  "time": Record.timestamp,
  "func_name": Record.identifier,
  "msg": Record.message,
  "lvl": {
    "lname": Record.level.name,
    "limportanity": Record.level.importance
  }
}
```

last but not least put everything into one `LevelModel`

```python
my_level_model: LevelModel = LevelModel(
    model=my_new_level,
    request_meta=my_new_request_meta,
    request_model=my_new_request_model
)
```

finally, add your brand new level into Tekek

```python
logger = Tekek(__name__)
logger.add_level(my_new_level)
```