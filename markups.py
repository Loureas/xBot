from aiogram.types.inline_keyboard import (InlineKeyboardMarkup,
                                           InlineKeyboardButton)
from localization import local
from config import config

def report_menu_ikbd(message_id: int, reporter_user_id: int, violator_user_id: int):
    buttons = [
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_del"]["text"],
                callback_data=local[config.lang]["action_del"]["data"].format(
                    message_id=message_id
                )
            )

        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_del_mute_1h"]["text"],
                callback_data=local[config.lang]["action_del_mute_1h"]["data"].format(
                    message_id=message_id,
                    user_id=violator_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_del_mute_1d"]["text"],
                callback_data=local[config.lang]["action_del_mute_1d"]["data"].format(
                    message_id=message_id,
                    user_id=violator_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_del_mute_1w"]["text"],
                callback_data=local[config.lang]["action_del_mute_1w"]["data"].format(
                    message_id=message_id,
                    user_id=violator_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_del_ban"]["text"],
                callback_data=local[config.lang]["action_del_ban"]["data"].format(
                    message_id=message_id,
                    user_id=violator_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_dis"]["text"],
                callback_data=local[config.lang]["action_dis"]["data"]
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_dis_mute_1h"]["text"],
                callback_data=local[config.lang]["action_dis_mute_1h"]["data"].format(
                    user_id=reporter_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_dis_mute_1d"]["text"],
                callback_data=local[config.lang]["action_dis_mute_1d"]["data"].format(
                    user_id=reporter_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_dis_mute_1w"]["text"],
                callback_data=local[config.lang]["action_dis_mute_1w"]["data"].format(
                    user_id=reporter_user_id
                )
            )
        ],
        [
            InlineKeyboardButton(
                text=local[config.lang]["action_dis_ban"]["text"],
                callback_data=local[config.lang]["action_dis_ban"]["data"].format(
                    user_id=reporter_user_id
                )
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

