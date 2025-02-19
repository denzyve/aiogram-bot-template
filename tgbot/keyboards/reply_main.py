# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.data.config import get_admins
from tgbot.utils.const_functions import rkb


# Кнопки главного меню
def menu_frep(user_id) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.row(
        rkb("Профиль"), rkb("2"),
    ).row(
        rkb("3"), rkb("4")
    )

    if user_id in get_admins():
        keyboard.row(
            rkb("Админ"), rkb("/db"), rkb("/log"),
        )

    return keyboard.as_markup(resize_keyboard=True)


