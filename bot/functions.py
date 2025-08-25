from asgiref.sync import sync_to_async

from common.models import TelegramUser


@sync_to_async
def get_or_create_user(telegram_user_id):
    return TelegramUser.objects.get_or_create(telegram_user_id=telegram_user_id)


@sync_to_async
def get_user(telegram_user_id):
    return TelegramUser.objects.get(telegram_user_id=telegram_user_id)
