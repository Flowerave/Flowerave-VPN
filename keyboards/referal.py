from aiogram import types

from loader import vote_cb

referal = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('выплата по рефералам', callback_data=vote_cb.new(action='ref_pay'))
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='start'))
)
