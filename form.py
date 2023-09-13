import logging
from typing import Any, Dict

from aiogram import F, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()


class States(StatesGroup):
    name = State()


@router.message(States.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Main form name",
        reply_markup=ReplyKeyboardRemove())    
    