from aiogram import Bot, Dispatcher
import config
from aiogram.utils.callback_data import CallbackData
from utils.db_api.db_gino import db

vote_cb = CallbackData('vote', 'action')

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

__all__ = ['bot', 'db', 'dp', 'vote_cb']
