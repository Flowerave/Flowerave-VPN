from aiogram import types
from loader import vote_cb

start = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('получить впн', callback_data=vote_cb.new(action='get_vpn')),
).row(
    types.InlineKeyboardButton('тарифные планы', callback_data=vote_cb.new(action='tariffs')),
    types.InlineKeyboardButton('рефралОчка', callback_data=vote_cb.new(action='refs')),
).row(
    types.InlineKeyboardButton('саппорт', callback_data=vote_cb.new(action='support')),
    types.InlineKeyboardButton('настройки', callback_data=vote_cb.new(action='settings')),
)
