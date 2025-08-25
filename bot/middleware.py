from aiogram import BaseMiddleware

from bot.functions import get_or_create_user


class UserCreateMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        telegram_user_id = event.from_user.id
        await get_or_create_user(telegram_user_id)

        return await handler(event, data)

