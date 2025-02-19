# - *- coding: utf- 8 - *-
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.keyboards.reply_main import menu_frep
from tgbot.utils.bot_models import FSM

router = Router(name=__name__)


# Открытие главного меню
@router.message(F.text == '🔙 Главное меню')
@router.message(Command(commands=['start']))
async def main_start(message: Message, state: FSM):
    await state.clear()

    await message.answer("➖ Главное меню", reply_markup=menu_frep(user_id=message.from_user.id))
