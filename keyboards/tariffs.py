from aiogram import types

from loader import vote_cb

tariffs = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('тариф 1', callback_data=vote_cb.new(action='tariff_one')),
    types.InlineKeyboardButton('тариф 2', callback_data=vote_cb.new(action='tariff_tow'))
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='tariffs'))
)
