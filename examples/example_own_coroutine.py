import asyncio
from .tekek import Tekek


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
