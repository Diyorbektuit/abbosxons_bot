from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


async def start_keyboard(x_api_key):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Qo'shilish",
                    web_app=WebAppInfo(
                        url=f"https://preview--responsive-app-builder.lovable.app/?x_api_key={x_api_key}"
                    )
                ),
            ],
        ],
    )

    return keyboard