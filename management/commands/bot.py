from django.core.management.base import BaseCommand
import asyncio
import logging


from ...bot import main


class Command(BaseCommand):
    args = ""
    help = "Bot daemon"

    def handle(self, *args, **options):
        logging.info(f"{self.help} started")
        main()
