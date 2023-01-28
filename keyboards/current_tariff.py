from aiogram import types

from loader import vote_cb

current_tariff = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('изменить тариф', callback_data=vote_cb.new(action='change_tariff'))
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='start'))
)
