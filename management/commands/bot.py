from django.core.management.base import BaseCommand
import asyncio
import logging


from ...bot import run


class Command(BaseCommand):
    args = ""
    help = "Bot daemon"

    def handle(self, *args, **options):
        logging.info(f"{self.help} started")
        try:
            asyncio.run(run())
        except (KeyboardInterrupt, SystemExit):
            logging.warning("Bot interrupted")
        except Exception as e:
            logging.warning(e)
