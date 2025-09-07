import time
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


def create_invite_link():
    url = f"https://api.telegram.org/bot{BaseConfig.BOT_TOKEN}/createChatInviteLink"

    expire_time = int(time.time()) + 86400
    member_limit = 1

    params = {
        'chat_id': BaseConfig.MAIN_CHANNEL_ID,
        'name': 'Private Channel Invite',
        'expire_date': expire_time,
        'member_limit': member_limit,
        'creates_join_request': False
    }

    response = requests.post(url, json=params)
    return response.json()


def send_telegram_bot_message(user_chat_id: int, invite_link: str):
    url = f"https://api.telegram.org/bot{BaseConfig.BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": user_chat_id,
        "text": f"Kanalga qo'shilish uchun invite linkni bosing: {invite_link}"
    }

    response = requests.post(url, json=data).json()
    print(response)
    return response

