from aiogram import Bot, Dispatcher
import config
from aiogram.utils.callback_data import CallbackData

vote_cb = CallbackData('vote', 'action')

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
