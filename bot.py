from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys
import os

try:
    from .middleware import AuthMiddleware
    from .examples.echo import echo_router
    from .examples.fsm import form_router
except ImportError:
    from middleware import AuthMiddleware
    from examples.echo import echo_router
    from examples.fsm import form_router


async def run():
    token = os.environ["TELEGRAM_TOKEN"]
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=token, default=default)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(
        form_router,
        echo_router,
    )
    await dp.start_polling(bot)


def main():
    try:
        asyncio.run(run())
    except (KeyboardInterrupt, SystemExit):
        logging.warning("Bot interrupted")


if __name__ == "__main__":
    level = os.getenv("LOG_LEVEL", logging.INFO)
    logging.basicConfig(
        level=level, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    main()
