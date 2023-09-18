from aiogram import BaseMiddleware
from secrets import authorized_users
import logging


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.from_user.id not in authorized_users.values():
            logging.warning(
                f"{event.from_user.username} id {event.from_user.id} not authorized"
            )
            return
        return await handler(event, data)
