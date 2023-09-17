import asyncio
import logging
import sys

from middleware.auth import AuthMiddleware
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

from authorization_keys import BOT_TOKEN
from commands.echo import echo_router


async def main() -> None:
    token = BOT_TOKEN
    bot = Bot(token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(
        echo_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    asyncio.run(main())
