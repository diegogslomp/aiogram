import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

echo_router = Router()

@echo_router.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


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
