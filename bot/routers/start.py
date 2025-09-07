from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.texts.start import start_text
from bot.keyboards.start import start_keyboard
from bot.functions import get_user

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    user = await get_user(message.from_user.id)
    keyboard = await start_keyboard(x_api_key=user.x_api_key)
    await message.answer_photo(
        photo="https://api.xazratqulov.uz/media/images/Creators_Pro.png",
        caption=start_text(),
        reply_markup=keyboard
    )