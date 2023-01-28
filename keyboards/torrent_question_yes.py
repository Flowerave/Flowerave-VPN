from aiogram import types

from loader import vote_cb

torrent_question_yes = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton('страна 1', callback_data=vote_cb.new(action='send_config')),
    types.InlineKeyboardButton('страна 2', callback_data=vote_cb.new(action='send_config'))
).row(
    types.InlineKeyboardButton('назад', callback_data=vote_cb.new(action='get_vpn'))
)
