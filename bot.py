import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from commands.echo import echo_router


async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    asyncio.run(main())
