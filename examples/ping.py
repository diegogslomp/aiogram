from aiogram import F, Router, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
import platform
import string
import subprocess


router = Router()


class Form(StatesGroup):
    ping = State()


def sanitize(dirty: str) -> str:
    clean = ""
    whitelist = string.ascii_letters + string.digits + "-" + "_" + "."
    for char in dirty:
        if char in whitelist:
            clean += char
    return clean


@router.message(Command("ping"))
async def ask_host(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.ping)

    await message.answer(
        "Inform host or ip",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.ping)
async def ping(message: Message, state: FSMContext) -> None:
    await state.clear()

    host = sanitize(message.text)
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    stdout = subprocess.DEVNULL
    stderr = subprocess.STDOUT

    online = subprocess.call(command, stdout=stdout, stderr=stderr) == 0

    return_message = "🟢 Up" if online else "🔴 Down"

    await message.answer(
        f"{html.quote(return_message)}",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()

    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )
