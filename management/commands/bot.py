from django.core.management.base import BaseCommand
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import asyncio
import logging
import os


from ...middleware import AuthMiddleware
from ...command.echo import echo_router
from ...main import main



class Command(BaseCommand):
    args = ""
    help = "Question daemon"

    def handle(self, *args, **options):
        logging.info(f"{self.help} started")
        try:
            asyncio.run(main())
        except (KeyboardInterrupt, SystemExit):
            logging.warning("Bot interrupted")
        except Exception as e:
            logging.warning(e)
