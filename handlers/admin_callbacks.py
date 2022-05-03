from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import (MessageCantBeDeleted,
                                      MessageToDeleteNotFound)
from dispatcher import dp
from config import config
from localization import local
from contextlib import suppress
from time import time

@dp.callback_query_handler(Text(startswith="del_"), chat_id=config.admin_chat)
async def delete_message(call: types.CallbackQuery):
    msg_id = int(call.data.split("_")[1])
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await call.message.bot.delete_message(config.main_chat, msg_id)
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_del"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="delmute_1h_"), chat_id=config.admin_chat)
async def delete_mute_1h(call: types.CallbackQuery):
    msg_id, user_id = map(int, call.data.split("_")[2:])
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await call.message.bot.delete_message(config.main_chat, msg_id)
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + 3600)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_del_mute_1h"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="delmute_1d_"), chat_id=config.admin_chat)
async def delete_mute_1d(call: types.CallbackQuery):
    msg_id, user_id = map(int, call.data.split("_")[2:])
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await call.message.bot.delete_message(config.main_chat, msg_id)
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + 3600*24)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_del_mute_1d"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="delmute_1w_"), chat_id=config.admin_chat)
async def delete_mute_1w(call: types.CallbackQuery):
    msg_id, user_id = map(int, call.data.split("_")[2:])
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await call.message.bot.delete_message(config.main_chat, msg_id)
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + (3600*24)*7)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_del_mute_1w"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="delban_"), chat_id=config.admin_chat)
async def delete_ban(call: types.CallbackQuery):
    msg_id, user_id = map(int, call.data.split("_")[1:])
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await call.message.bot.delete_message(config.main_chat, msg_id)
    await call.message.bot.ban_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        revoke_messages=True
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_del_ban"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="dismiss"), chat_id=config.admin_chat)
async def dismiss(call: types.CallbackQuery):
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_dis"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="dismute_1h_"), chat_id=config.admin_chat)
async def dismute_1h(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[2])
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + 3600)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_dis_mute_1h"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="dismute_1d_"), chat_id=config.admin_chat)
async def dismute_1d(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[2])
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + 3600*24)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_dis_mute_1d"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="dismute_1w_"), chat_id=config.admin_chat)
async def dismute_1w(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[2])
    await call.message.bot.restrict_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        permissions=types.ChatPermissions(),
        until_date=int(time() + (3600*24)*7)
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_dis_mute_1w"]["text"]
        )
    )

@dp.callback_query_handler(Text(startswith="disban_"), chat_id=config.admin_chat)
async def disban(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[1])
    await call.message.bot.ban_chat_member(
        chat_id=config.main_chat,
        user_id=user_id,
        revoke_messages=True
    )
    await call.message.edit_text(
        call.message.html_text
        + "\n" + local[config.lang]["decision_is_made"].format(
            decision=local[config.lang]["action_dis_ban"]["text"]
        )
    )

