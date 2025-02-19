# - *- coding: utf- 8 - *-
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message

from tgbot.utils.const_functions import del_message, ded

router = Router(name=__name__)


# Колбэк с удалением сообщения
@router.callback_query(F.data == "close_this")
async def main_missed_callback_close(call: CallbackQuery):
    await del_message(call.message)


# Колбэк с обработкой кнопки
@router.callback_query(F.data == "...")
async def main_missed_callback_answer(call: CallbackQuery):
    await call.answer(cache_time=60)


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@router.callback_query(StateFilter("*"))
async def main_missed_callback(call: CallbackQuery):
    await call.answer("❗️ Кнопка недействительна. Повторите действия заново", True)


# Обработка всех неизвестных команд
@router.message()
async def main_missed_message(message: Message):
    await message.answer(
        ded(f"""
            ♦️ Неизвестная команда.
            ♦️ Введите /start
        """),
    )

