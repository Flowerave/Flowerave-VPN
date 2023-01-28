from aiogram import types

from loader import vote_cb

pay = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='tariffs'))
)
