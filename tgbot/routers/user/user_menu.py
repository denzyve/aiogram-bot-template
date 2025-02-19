# - *- coding: utf- 8 - *-
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.utils.bot_models import FSM


router = Router(name=__name__)

# Открытие профиля
@router.message(F.text == "Профиль")
@router.message(Command(commands=['profile']))
async def user_profile(message: Message, state: FSM):
    await state.clear()

    await message.answer("Профиль")
    