import inspect

from sanic import Sanic
from fastapi import FastAPI

from tekek import Tekek
from tekek import LOG, DEBUG, INFO, WARNING, ERROR, EXCEPTION, CRITICAL


class TestHelloWorld:
    def test_instantiation(self):
        logger = Tekek("Instantiation_Test")

        assert logger.name == "Instantiation_Test"
        assert isinstance(logger, Tekek)

    def test_logging_function_avaibility(self):
        logger = Tekek("Instantiation_Test")

        assert inspect.ismethod(logger.log)
        assert inspect.ismethod(logger.debug)
        assert inspect.ismethod(logger.info)
        assert inspect.ismethod(logger.warning)
        assert inspect.ismethod(logger.error)
        assert inspect.ismethod(logger.exception)
        assert inspect.ismethod(logger.critical)

    def test_logging(self):
        logger = Tekek("Instantiation_Test")

        _log, _log_o = logger.log("MESSAGE")
        _debug, _debug_o = logger.debug("MESSAGE")
        _info, _info_o = logger.info("MESSAGE")
        _warning, _warning_o = logger.warning("MESSAGE")
        _error, _error_o = logger.error("MESSAGE")
        _exception, _exception_o = logger.exception("MESSAGE")
        _critical, _critical_o = logger.critical("MESSAGE")

        # Check if all function return True
        assert _log
        assert _debug
        assert _info
        assert _warning
        assert _error
        assert _exception
        assert _critical

        # Check if all function return the correct level
        assert _log_o == LOG
        assert _debug_o == DEBUG
        assert _info_o == INFO
        assert _warning_o == WARNING
        assert _error_o == ERROR
        assert _critical_o == CRITICAL
        assert _exception_o == EXCEPTION


class TestCompatibilitySanic:
    # TODO: Write better sanic compatibility unit test
    def test_sanic(self):
        app = Sanic("Sanic_Test_App")

        assert isinstance(app, Sanic)

    def test_compatibility_sanic(self):
        app = Sanic("Sanic_Test_App")
        logger = Tekek("Tekek_Compatibility", app=app)

        assert logger.compatibility_mode


class TestCompatibilityFastAPI:
    # TODO: Write better compatibility test for fast api
    def test_fast_api(self):
        app = FastAPI()

        assert isinstance(app, FastAPI)

    def test_compatibility_fast_api(self):
        app = FastAPI()
        logger = Tekek("Tekek_Compatibility", app=app)

        assert logger.compatibility_mode


class TestCompatibilityOwn:
    def test_coroutine(self):
        import asyncio

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

        try:
            assert isinstance(logger, Tekek)
            assert asyncio.iscoroutine(my_app(3))
            assert asyncio.iscoroutine(main())
            assert asyncio.iscoroutine(logger.start())

            asyncio.run(main())

            assert logger.running
        except:
            assert False

    def test_class(self):
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

        assert isinstance(logger, Tekek)
        assert asyncio.iscoroutine(my_app.start())
        assert asyncio.iscoroutine(my_app.app())
        assert asyncio.iscoroutine(main())


        asyncio.run(main())