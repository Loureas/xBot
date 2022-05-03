from aiogram import types
from dispatcher import dp
from config import config
from localization import local
from contextlib import suppress

@dp.message_handler(chat_id=config.main_chat, content_types="new_chat_members")
async def on_user_join(message: types.Message):
    await message.delete()
    welcome_text = ""
    rules_text = ""
    with suppress(FileNotFoundError):
        welcome_text = open(config.welcome_file).read().strip()
        rules_text = open(config.rules_file).read().strip()
    if not welcome_text:
        await message.bot.send_message(
            config.admin_chat,
            local[config.lang]["welcome_no_exists"]
        )
        return
    msg_answer = local[config.lang]["welcome_caption"].format(
        user_id=message.from_user.id,
        user_name=message.from_user.first_name,
        text=welcome_text
    )
    if rules_text:
        msg_answer += "\n\n" + local[config.lang]["rules_caption"].format(
            text=rules_text
        )
    else:
        await message.bot.send_message(
            config.admin_chat,
            local[config.lang]["rules_no_exists"]
        )
    await message.answer(
        msg_answer + "\n\n" + local[config.lang]["help_commands"],
        disable_web_page_preview=True
    )

