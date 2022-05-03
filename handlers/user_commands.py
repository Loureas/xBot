import random

from aiogram import types
from dispatcher import dp
from config import config
from localization import local
from contextlib import suppress
from markups import *
from utils import *

@dp.message_handler(chat_id=config.main_chat, commands="rules")
async def show_rules(message: types.Message):
    rules = ""
    with suppress(FileNotFoundError):
        rules = open(config.rules_file).read().strip()
    if not rules:
        await message.bot.send_message(
            config.admin_chat,
            local[config.lang]["rules_no_exists"]
        )
        return
    await message.reply(rules, disable_web_page_preview=True)

@dp.message_handler(chat_id=config.main_chat, commands="help")
async def show_help(message: types.Message):
    msg_answer = local[config.lang]["help_commands"]
    member = await message.bot.get_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id
    )
    if member.is_chat_admin():
        msg_answer += local[config.lang]["help_admin_commands"]
    await message.reply(msg_answer)

@dp.message_handler(chat_id=config.main_chat, commands="report")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply(local[config.lang]["error_no_reply"])
        return
    user = await message.bot.get_chat_member(
        message.reply_to_message.chat.id,
        message.reply_to_message.from_user.id
    )
    if user.is_chat_admin():
        await message.reply(
            random.choice(local[config.lang]["error_report_admin"])
        )
        return
    if message.from_user.id == message.reply_to_message.from_user.id:
        await message.reply(
            random.choice(local[config.lang]["error_report_self"])
        )
        return
    report_message = local[config.lang]["new_report_from"].format(
        reporter_id=message.from_user.id,
        reporter_name=message.from_user.first_name
    )
    parts = message.text.split()
    if len(parts) > 1:
        report_message += local[config.lang]["report_message"].format(
            report_message=" ".join(parts[1:])[:101]
        )
    report_message += local[config.lang]["report_msg_link"].format(
        chat_id=get_url_chat_id(message.reply_to_message.chat.id),
        message_id=message.reply_to_message.message_id
    )
    await message.reply_to_message.forward(config.admin_chat)
    await message.bot.send_message(
        config.admin_chat,
        report_message,
        reply_markup=report_menu_ikbd(
            message_id=message.reply_to_message.message_id,
            violator_user_id=message.reply_to_message.from_user.id,
            reporter_user_id=message.from_user.id
        )
    )
    answer_text = local[config.lang]["report_sent"]
    if len(" ".join(parts[1:])) > 100:
        answer_text += local[config.lang]["report_text_limit"]
    await message.reply(answer_text)

@dp.message_handler(chat_id=config.main_chat, commands="attention")
async def attract_admins(message: types.Message):
    if message.reply_to_message:
        msg_id = message.reply_to_message.message_id
    else:
        msg_id = message.message_id
    await message.bot.send_message(
        config.admin_chat,
        local[config.lang]["attention_admin"].format(
            chat_id=get_url_chat_id(message.chat.id),
            message_id=msg_id
        )
    )
    await message.reply(
        local[config.lang]["wait_admins"]
    )

@dp.message_handler(is_admin=False, chat_id=config.main_chat, commands=["mute", "ban"])
async def user_cant_restrict(message: types.Message):
    await message.reply(local[config.lang]["user_cant_restrict"])

