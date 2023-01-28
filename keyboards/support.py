from aiogram import types

from loader import vote_cb

support = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('написать в поддержку', callback_data=vote_cb.new(action='real_supp')),
    types.InlineKeyboardButton('FAQ', callback_data=vote_cb.new(action='FAQ')),
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='start'))
)
