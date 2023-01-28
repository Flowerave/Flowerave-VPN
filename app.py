import logging

from aiogram import executor

from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from loader import db
from utils.db_api.db_gino import on_startup_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


async def on_startup(dp):
    await set_default_commands(dp)
    await on_startup_db(dp)
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
