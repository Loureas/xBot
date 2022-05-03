import random

from aiogram import types
from dispatcher import dp
from config import config
from localization import local
from time import time

@dp.message_handler(chat_id=config.admin_chat, commands="help")
async def help_admin_chat(message: types.Message):
    await message.reply(local[config.lang]["help_admin_chat_commands"])

@dp.message_handler(is_admin=True, chat_id=config.main_chat, commands="mute")
async def mute_user(message: types.Message):
    if not message.reply_to_message:
        await message.reply(local[config.lang]["error_no_reply"])
        return
    if message.from_user.id == message.reply_to_message.from_user.id:
        await message.reply(
            random.choice(local[config.lang]["error_report_self"])
        )
        return
    user = await message.bot.get_chat_member(
        message.reply_to_message.chat.id,
        message.reply_to_message.from_user.id
    )
    if user.is_chat_admin():
        await message.reply(
            random.choice(local[config.lang]["error_admin_to_admin"])
        )
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) > 1:
        if parts[1] not in ["1h", "1d", "1w"]:
            await message.reply(local[config.lang]["error_mute_period"])
            return
        if parts[1] == "1h":
            await message.bot.restrict_chat_member(
                chat_id=message.reply_to_message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=types.ChatPermissions(),
                until_date=int(time() + 3600)
            )
        elif parts[1] == "1d":
            await message.bot.restrict_chat_member(
                chat_id=message.reply_to_message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=types.ChatPermissions(),
                until_date=int(time() + 3600*24)
            )
        elif parts[1] == "1w":
            await message.bot.restrict_chat_member(
                chat_id=message.reply_to_message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=types.ChatPermissions(),
                until_date=int(time() + (3600*24)*7)
            )
    else:
        await message.bot.restrict_chat_member(
            chat_id=message.reply_to_message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=types.ChatPermissions(),
            until_date=int(time() + 3600)
        )
    await message.reply(local[config.lang]["mute_success"])

@dp.message_handler(is_admin=True, chat_id=config.main_chat, commands="ban")
async def ban_user(message: types.Message):
    if not message.reply_to_message:
        await message.reply(local[config.lang]["error_no_reply"])
        return
    if message.from_user.id == message.reply_to_message.from_user.id:
        await message.reply(
            random.choice(local[config.lang]["error_report_self"])
        )
        return
    user = await message.bot.get_chat_member(
        message.reply_to_message.chat.id,
        message.reply_to_message.from_user.id
    )
    if user.is_chat_admin():
        await message.reply(
            random.choice(local[config.lang]["error_admin_to_admin"])
        )
        return
    await message.bot.ban_chat_member(
        chat_id=message.reply_to_message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        revoke_messages=True
    )
    await message.reply(local[config.lang]["ban_success"])

@dp.message_handler(chat_id=config.admin_chat, commands="setrules")
async def set_rules(message: types.Message):
    parts = message.html_text.split(maxsplit=1)
    if len(parts) == 1:
        await message.reply(local[config.lang]["enter_text"])
        return
    rules_text = parts[1].strip()
    open(config.rules_file, "w").write(rules_text)
    await message.reply(local[config.lang]["rules_set_success"])
    msg_rules = await message.bot.send_message(
        config.main_chat,
        local[config.lang]["rules_warning"].format(
            rules=rules_text
        ),
        disable_web_page_preview=True
    )
    await msg_rules.pin()

@dp.message_handler(chat_id=config.admin_chat, commands="setwelcome")
async def set_welcome(message: types.Message):
    parts = message.html_text.split(maxsplit=1)
    if len(parts) == 1:
        await message.reply(local[config.lang]["enter_text"])
        return
    welcome_text = parts[1].strip()
    open(config.welcome_file, "w").write(welcome_text)
    await message.reply(local[config.lang]["welcome_set_success"])

