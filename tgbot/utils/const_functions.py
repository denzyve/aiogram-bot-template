# - *- coding: utf- 8 - *-
import pytz
from datetime import datetime

from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton

from tgbot.data.config import get_admins, BOT_TIMEZONE

def rkb(text: str) -> KeyboardButton:
    return KeyboardButton(text=text)

# Удаление сообщения с обработкой ошибок от телеграма
async def del_message(message: Message):
    try:
        await message.delete()
    except:
        ...


# Отправка сообщения всем админам
async def send_admins(bot: Bot, text: str, keyboard: InlineKeyboardMarkup = None, not_me: int = 0):
    for admin in get_admins():
        try:
            if str(admin) != str(not_me):
                await bot.send_message(
                    admin,
                    text,
                    reply_markup=keyboard,
                    disable_web_page_preview=True,
                )
        except:
            ...


# Удаление отступов у текста
def ded(get_text: str) -> str:
    if get_text is not None:
        split_text = get_text.split("\n")

        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop()
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)
    else:
        get_text = ""

    return get_text

def get_date(full: bool = True) -> str:
    if full:  # Полная дата с временем
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d.%m.%Y %H:%M:%S")
    else:  # Только дата без времени
        return datetime.now(pytz.timezone(BOT_TIMEZONE)).strftime("%d.%m.%Y")
    