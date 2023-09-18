from middleware.auth import AuthMiddleware
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys
import os


from command.echo import echo_router


async def main():
    level = os.getenv("LOG_LEVEL", logging.INFO)
    logging.basicConfig(
        level=level, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    token = os.environ["BOT_TOKEN"]
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(
        echo_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
