local = {
    "ru" : {
        "welcome_caption" : "<b><a href=\"tg://user?id={user_id}\">{user_name}</a>, добро пожаловать в чат!</b> 👋🏻\n{text}",
        "rules_caption" : "☝️ <b>Правила:</b>\n{text}",

        "help_commands" : ("🤖 <i>Доступные команды бота:</i>\n"
                           "/rules — <i>вывести правила</i>\n"
                           "/help — <i>вывести доступные команды</i>\n"
                           "/report <code>[комментарий до 100 символов]</code> — <i>отправить жалобу на пользователя (необходимо ответное сообщение)</i>\n"
                           "/attention — <i>привлечь внимание админов (необязательно с ответным сообщением)</i>\n"),
        "help_admin_commands" : ("/mute <code>[1h - час, 1d - день, 1w - неделю]</code> — <i>Выдать мут пользователю (необходимо ответное сообщение, только для админов)</i>\n"
                                 "/ban — <i>Выдать бан пользователю (необходимо ответное сообщение, только для админов)</i>\n"),
        "help_admin_chat_commands" : ("/setrules <code>текст правил</code> — <i>установить правила (допускается форматирование)</i>\n"
                                      "/setwelcome <code>текст приветствия</code> — <i>установить приветственное сообщение (допускается форматирование)</i>"),

        "error_no_reply" : "<i>Необходимо ответное сообщение пользователя для выполнения данной команды</i>",
        "error_report_admin" : [
            "Ты хоть понимаешь, что делаешь? 🤨",
            "Нельзя жаловаться на всемогущих! 😈",
            "За тобой выехали... 🔴🔵",
            "На кого руку поднял? Щенок 🤨"
        ],
        "error_report_self" : [
            "Ох, рискованно-рискованно 😏",
            "Как ты себе это представляешь? 🤓",
            "Ну все, adios! 👋🏻",
            "Давай ты ещё выйдешь из группы напоследок)"
        ],

        "new_report_from" : "⚠️ <b>Новый репорт от <a href=\"tg://user?id={reporter_id}\">{reporter_name}</a></b>\n",
        "report_message" : "<b>Комментарий от репортера:</b> {report_message}\n",
        "report_msg_link" : "<a href=\"tg://privatepost?channel={chat_id}&post={message_id}\">Перейти к сообщению</a>",
        "report_sent" : "<i>Репорт отправлен</i>\n",
        "report_text_limit" : "<i>Примечание: комментарий к вашей жалобе был обрезан до лимита длины текста</i>",

        "action_del" : {
            "text" : "🗑 Удалить",
            "data" : "del_{message_id}"
        },
        "action_del_mute_1h" : {
            "text" : "🗑 Удалить + 🔇 мут на час",
            "data" : "delmute_1h_{message_id}_{user_id}"
        },
        "action_del_mute_1d" : {
            "text" : "🗑 Удалить + 🔇 мут на день",
            "data" : "delmute_1d_{message_id}_{user_id}"
        },
        "action_del_mute_1w" : {
            "text" : "🗑 Удалить + 🔇 мут на неделю",
            "data" : "delmute_1w_{message_id}_{user_id}"
        },
        "action_del_ban" : {
            "text" : "🗑 Удалить + ⛔️ бан",
            "data" : "delban_{message_id}_{user_id}"
        },

        "action_dis" : {
            "text" : "✅ Чисто",
            "data" : "dismiss"
        },
        "action_dis_mute_1h" : {
            "text" : "✅ Чисто + 🔇 мут репортера на час",
            "data" : "dismute_1h_{user_id}"
        },
        "action_dis_mute_1d" : {
            "text" : "✅ Чисто + 🔇 мут репортера на день",
            "data" : "dismute_1d_{user_id}"
        },
        "action_dis_mute_1w" : {
            "text" : "✅ Чисто + 🔇 мут репортера на неделю",
            "data" : "dismute_1w_{user_id}"
        },
        "action_dis_ban" : {
            "text" : "✅ Чисто + ⛔️ бан репортера",
            "data" : "disban_{user_id}"
        },

        "decision_is_made" : "☑️ <b>Решение принято:</b> {decision}",

        "attention_admin" : ("⚠️ <b>Админы, нужно ваше присутствие</b>\n"
                             "<a href=\"tg://privatepost?channel={chat_id}&post={message_id}\">Перейти к сообщению</a>"),
        "wait_admins" : "<i>Ожидайте прибытия админов</i>",

        "mute_success" : "🔇 <i>Мут выдан</i>",
        "ban_success" : "⛔️ <i>Бан выдан</i>",
        "error_mute_period" : ("<i>Неверный период действия мута. Доступно:\n"
                               "1h - на час\n"
                               "1d - на день\n"
                               "1w - на неделю</i>"),
        "error_admin_to_admin" : [
            "Админ на Админа = 🤯🤯🤯",
            "Моя логика сломалась от такой команды... 🤔🧐",
            "⚔️ <b>Началось великое противостояние</b> ⚔️",
            "Девоцки, успокойтесь"
        ],
        "user_cant_restrict" : "У тебя здесь нет власти! 😈",

        "enter_text" : ("<i>Введите текст\n"
                        "Допускается форматирование</i>"),

        "rules_no_exists" : "⚠️ <b>Админы, правила отсутствуют! Настоятельно рекомендуется установить их с помощью команды</b> /setrules",
        "rules_set_success" : "<i>Правила установлены</i>",
        "rules_warning" : "⚠️ <b>Внимание! Обновлены правила!</b>\n\n{rules}",

        "welcome_no_exists" : ("<b>Новый участник присоединился, однако приветственное сообщение отсутствует</b>\n"
                               "Для его установки — используйте команду /setwelcome"),
        "welcome_set_success" : "<i>Приветственное сообщение установлено</i>",

        "new_video_1" : "🔥 <b>Новое видео на канале <a href=\"{channel_url}\">{channel_name}</a>!</b>",
        "new_video_2" : "🔥 <b>Новые видео на канале <a href=\"{channel_url}\">{channel_name}</a>!</b>",
        "action_play_video" : "▶️ Смотреть"
    },
    "video_info" : "🎞 <b><a href=\"{video_url}\">{video_title}</a></b>\n"
}

