from middleware.auth import AuthMiddleware
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys

from secrets import bot_token, log_level
from command.echo import echo_router


async def main():
    logging.basicConfig(
        level=log_level, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(
        echo_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
