from aiogram import types

from loader import vote_cb

settings = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('смена языка', callback_data=vote_cb.new(action='real_supp')),
    types.InlineKeyboardButton('удаление всех данных из бд', callback_data=vote_cb.new(action='FAQ')),
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='start'))
)
