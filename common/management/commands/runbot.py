import logging
import sys
import asyncio

from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher

from bot.routers import all_routers
from bot.middleware import UserCreateMiddleware
from settings import BaseConfig


class Command(BaseCommand):
    help = 'Start bot'

    def handle(self, *args, **kwargs):
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        stream_handler.stream = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

        logging.basicConfig(level=logging.INFO, handlers=[stream_handler])
        asyncio.run(self.start_bot())

    @staticmethod
    async def start_bot():
        bot = Bot(token=BaseConfig.BOT_TOKEN)

        dp = Dispatcher()

        for router in all_routers:
            dp.include_router(router)

        dp.message.middleware(UserCreateMiddleware())
        dp.callback_query.middleware(UserCreateMiddleware())

        await dp.start_polling(bot)

