from aiogram import BaseMiddleware
import logging
import ast
import os


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        authorized_users = ast.literal_eval(os.getenv("TELEGRAM_USERS", "{}"))

        if event.from_user.id not in authorized_users.values():
            logging.warning(
                f"{event.from_user.username} id {event.from_user.id} not authorized"
            )
            return
        return await handler(event, data)
