from authorization_keys import authorized_users
from aiogram import BaseMiddleware
import logging


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.from_user.id not in authorized_users.values():
            logging.warning(
                f"{event.from_user.username} id {event.from_user.id} is not in authorized keys"
            )
            return
        return await handler(event, data)
