from aiogram.fsm.context import FSMContext
from aiogram import Router, types
import logging

echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    logging.warning(f"id {message.from_user.id} echo f{message.text}")
    await state.clear()

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
