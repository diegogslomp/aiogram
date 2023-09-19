from aiogram.dispatcher.event.bases import SkipHandler, CancelHandler
from aiogram import BaseMiddleware
import logging
import ast
import os


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        authorized_users = ast.literal_eval(os.getenv("TELEGRAM_USERS", "{}"))

        if event.from_user.id not in authorized_users.values():
            logging.warning(
                f"User {event.from_user.username} id {event.from_user.id} not authorized"
            )
            raise SkipHandler()
        return await handler(event, data)
