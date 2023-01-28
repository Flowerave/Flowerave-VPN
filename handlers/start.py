import typing

from aiogram import types

from loader import dp
from loader import vote_cb
from keyboards import *


@dp.message_handler(text='/start')
async def cmd_panel(message: types.Message):
    await message.answer('Привет, это старовая панель VPN-бота', reply_markup=start)


@dp.callback_query_handler(
    vote_cb.filter(action=['get_vpn', 'tariffs', 'refs', 'support', 'settings', 'start', 'use_torrent',
                           'dont_use_torrent', 'send_config', 'change_tariff', 'tariff_one', 'tariff_tow',
                           'ref_pay', ]))
async def star_vote_action(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    chat_id = query.message.chat.id
    msg_id = query.message.message_id

    await query.answer()
    callback_data_action = callback_data['action']

    if callback_data_action == 'get_vpn':
        await dp.bot.edit_message_text('Ты будшь использовать torrent?', chat_id, msg_id,
                                       reply_markup=torrent_question)

    if callback_data_action == 'tariffs':
        await dp.bot.edit_message_text('В это сообщение из бд будет тянуться актуальный тариф',
                                       chat_id, msg_id, reply_markup=current_tariff)

    if callback_data_action == 'change_tariff':
        await dp.bot.edit_message_text('В этом сообщении будет описание разных тарифов (если их будет много)',
                                       chat_id, msg_id, reply_markup=tariffs)

    if callback_data_action == 'tariff_one':
        await dp.bot.edit_message_text('Здесь будет оплата, когда сделаю', chat_id, msg_id, reply_markup=pay)

    if callback_data_action == 'tariff_tow':
        await dp.bot.edit_message_text('Здесь будет оплата, когда сделаю', chat_id, msg_id, reply_markup=pay)

    if callback_data_action == 'refs':
        await dp.bot.edit_message_text('Список рефреалов из бд\nРеф ссылка \nБаланс из бд',
                                       chat_id, msg_id, reply_markup=referal)

    if callback_data_action == 'ref_pay':
        await dp.bot.edit_message_text('Еблан? У нас сервиса нет, какие рефералы?🤡',
                                       chat_id, msg_id, reply_markup=refs)

    if callback_data_action == 'support':
        await dp.bot.edit_message_text(
            'Всякие штуки для поддержки, думаю тут в кнопках ссылки будут или что ты там нарисуешь, так как логику мы '
            'не продумывали, кнопки пустые',
            chat_id, msg_id, reply_markup=support)

    if callback_data_action == 'settings':
        await dp.bot.edit_message_text(
            'Смену языка прямо сейчас делать не буду, да и не уверен что она нужна, бд нет, так что удалять тоже '
            'нечего, кнопки пустые',
            chat_id, msg_id, reply_markup=settings)

    if callback_data_action == 'start':
        await dp.bot.edit_message_text('Привет, это старовая панель VPN-бота', chat_id, msg_id, reply_markup=start)

    if callback_data_action == 'use_torrent':
        await dp.bot.edit_message_text('выбери страну)', chat_id, msg_id, reply_markup=torrent_question_yes)

    if callback_data_action == 'dont_use_torrent':
        await dp.bot.edit_message_text('выбери страну)', chat_id, msg_id, reply_markup=torrent_question_no)

    if callback_data_action == 'send_config':
        await dp.bot.edit_message_text('вот твой файл конфигурации:', chat_id, msg_id)
        # await dp.bot.send_document(chat_id, file)
        # await dp.bot.send_message(chat_id, 'конфиг присылается с компа моего, а не сервера(')
        # getkey(chat_id)
