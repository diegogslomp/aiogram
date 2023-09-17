from aiogram import Router, types
from aiogram.fsm.context import FSMContext

echo_router = Router()

@echo_router.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
