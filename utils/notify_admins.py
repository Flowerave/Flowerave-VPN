import logging

from aiogram import Dispatcher

from config import admins


async def on_startup_notify(dp: Dispatcher):
    text = 'Наталья морская пехота:\nСТАРТУЕМ!!!'
    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
