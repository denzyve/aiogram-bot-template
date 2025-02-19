# - *- coding: utf- 8 - *-
import configparser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_CONFIG = configparser.ConfigParser()
BOT_CONFIG.read("settings.ini")

BOT_TOKEN = BOT_CONFIG['settings']['BOT_TOKEN'].strip().replace(' ', '')
BOT_TIMEZONE = "Europe/Kiev"
BOT_SCHEDULER = AsyncIOScheduler(timezone=BOT_TIMEZONE)

PATH_DATABASE = "tgbot/data/database.db"
PATH_LOGS = "tgbot/data/logs.log"


def get_admins() -> list[int]:
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['ADMIN_ID'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins
