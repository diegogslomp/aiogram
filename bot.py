from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys
import os

try:
    from .middleware import AuthMiddleware
    from .command.echo import echo_router
except ImportError:
    from middleware import AuthMiddleware
    from command.echo import echo_router


async def run():
    token = os.environ["TELEGRAM_TOKEN"]
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(
        echo_router,
    )
    await dp.start_polling(bot)


def main():
    level = os.getenv("LOG_LEVEL", logging.INFO)
    logging.basicConfig(
        level=level, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    try:
        asyncio.run(run())
    except (KeyboardInterrupt, SystemExit):
        logging.warning("Bot interrupted")
    except Exception as e:
        logging.warning(e)


if __name__ == "__main__":
    main()
