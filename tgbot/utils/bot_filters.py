# - *- coding: utf- 8 - *-
from typing import Union

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from tgbot.data.config import get_admins


# Проверка на админа
class IsAdmin(BaseFilter):
    async def __call__(self, update: Union[Message, CallbackQuery], bot: Bot) -> bool:
        if update.from_user.id in get_admins():
            return True
        else:
            return False
