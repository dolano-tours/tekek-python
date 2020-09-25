import asyncio
from .tekek import Tekek


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
