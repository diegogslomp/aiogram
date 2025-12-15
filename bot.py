from aiogram.dispatcher.event.bases import SkipHandler, CancelHandler
from aiogram import Router, types, BaseMiddleware, Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
import asyncio
import logging
import dotenv
import sys
import ast
import os


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        authorized_users = ast.literal_eval(os.getenv("TELEGRAM_USERS", "{}"))
        if event.from_user.id not in authorized_users.values():
            logging.warning(
                f"No authorized user={event.from_user.username} id={event.from_user.id}"
            )
            raise SkipHandler()
        return await handler(event, data)


router = Router()


@router.message()
async def echo(message: types.Message, state: FSMContext) -> None:
    logging.warning(f"Echo id={message.from_user.id} msg=f{message.text}")
    await state.clear()
    try:
        await message.send_copy(chat_id=message.chat.id)
    except (TypeError, TelegramBadRequest):
        await message.answer("Nice try")


async def main():
    token = os.environ["TELEGRAM_TOKEN"]
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=token, default=default)
    dp = Dispatcher()
    dp.message.middleware(AuthMiddleware())
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    dotenv.load_dotenv()
    level = os.getenv("LOG_LEVEL", logging.INFO)
    logging.basicConfig(
        level=level, stream=sys.stdout, format="%(asctime)s %(message)s"
    )
    asyncio.run(main())
