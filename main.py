# - *- coding: utf- 8 - *-
import os
import sys
import asyncio
import colorama

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties

from tgbot.data.config import get_admins, BOT_TOKEN, BOT_SCHEDULER
from tgbot.middlewares import register_all_middlewares
from tgbot.routers import register_all_routers
from tgbot.utils.bot_commands import set_commands
from tgbot.utils.bot_logging import bot_logger

colorama.init()


async def scheduler_start(bot: Bot):
    pass # TODO: Add code here


async def main():
    BOT_SCHEDULER.start()
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

    register_all_middlewares(dp)
    register_all_routers(dp)

    try:
        await set_commands(bot)
        await scheduler_start(bot)

        bot_logger.warning("Bot was started.")
        print(colorama.Fore.LIGHTYELLOW_EX + f"~~~~~ Bot was started - @{(await bot.get_me()).username} ~~~~~")
        print(colorama.Fore.RESET)

        if len(get_admins()) == 0: print("***** ENTER ADMIN ID IN settings.ini *****")

        await bot.delete_webhook(drop_pending_updates=True)
        await bot.get_updates(offset=-1)

        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
        )
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        bot_logger.warning("Bot was stopped.")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")


