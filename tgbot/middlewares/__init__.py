# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from tgbot.middlewares.middleware_throttling import ThrottlingMiddleware


# Регистрация всех миддлварей
def register_all_middlewares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
