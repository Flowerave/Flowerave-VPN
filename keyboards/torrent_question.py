from aiogram import types

from loader import vote_cb

torrent_question = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('да', callback_data=vote_cb.new(action='use_torrent'))
).row(
    types.InlineKeyboardButton('нет', callback_data=vote_cb.new(action='dont_use_torrent'))
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='start'))
)
