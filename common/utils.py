import requests

from settings import BaseConfig


def add_to_channel(telegram_user_id: int):
    base_url = f"https://api.telegram.org/bot{BaseConfig.BOT_TOKEN}"
    url = f"{base_url}/approveChatJoinRequest"

    data = {
        "chat_id": BaseConfig.MAIN_CHANNEL_ID,
        "user_id": telegram_user_id
    }

    response = requests.get(url, json=data).json()
    print(response)
    return response


def remove_from_channel(telegram_user_id: int):
    base_url = f"https://api.telegram.org/bot{BaseConfig.BOT_TOKEN}"
    url = f"{base_url}/banChatMember"
    data = {
        "chat_id": BaseConfig.MAIN_CHANNEL_ID,
        "user_id": telegram_user_id,
        "until_date": 0
    }
    response = requests.get(url, json=data).json()
    return response
