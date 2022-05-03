import json
import asyncio

from dispatcher import bot
from config import config
from localization import local
from aiohttp import ClientSession
from contextlib import suppress
from io import BytesIO
from utils import fetch_bin
from aiogram.types.input_media import MediaGroup, InputMediaPhoto
from aiogram.types.inline_keyboard import (InlineKeyboardMarkup,
                                           InlineKeyboardButton)

YT_VIDEO_URL = "https://youtube.com/watch?v={video_id}"
YT_API_URL = "https://www.googleapis.com"
YT_API_PARAMS = {
    "key" : config.google_api_key,
    "channelId" : config.channel_id,
    "maxResults" : 10,
    "order" : "date",
    "type" : "video",
    "part" : "snippet",
    "fields" : ("items/id/videoId,"
                "items/snippet/title,"
                "items/snippet/thumbnails/high/url")
}
LAST_VIDEO_FILE = "last_video"

async def yt_notify_video():
    async with ClientSession(YT_API_URL) as session:
        async with session.get("/youtube/v3/search",
                               params=YT_API_PARAMS) as resp:
            res = await resp.text()
    res = json.loads(res)
    if not res["items"]:
        return
    last_video_id = ""
    with suppress(FileNotFoundError):
        last_video_id = open(LAST_VIDEO_FILE).read().strip()
    if not last_video_id:
        open(LAST_VIDEO_FILE, "w").write(res["items"][0]["id"]["videoId"])
        return
    new_video = []
    for video in res["items"]:
        if video["id"]["videoId"] == last_video_id:
            break
        new_video.append({
            "id" : video["id"]["videoId"],
            "url" :  YT_VIDEO_URL.format(video_id=video["id"]["videoId"]),
            "title" : video["snippet"]["title"],
            "thumbnail" : video["snippet"]["thumbnails"]["high"]["url"]
        })
    if not new_video:
        return
    open(LAST_VIDEO_FILE, "w").write(new_video[0]["id"])
    if len(new_video) == 1:
        msg_text = local[config.lang]["new_video_1"].format(
            channel_url=config.channel_url,
            channel_name=config.channel_name
        ) + "\n\n"
        markup = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    local[config.lang]["action_play_video"],
                    new_video[0]["url"]
                )
            ]]
        )
    else:
        msg_text = local[config.lang]["new_video_2"].format(
            channel_url=config.channel_url,
            channel_name=config.channel_name
        ) + "\n\n"
    for video in new_video:
        msg_text += local["video_info"].format(
            video_url=video["url"],
            video_title=video["title"]
        )
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch_bin(session, video["thumbnail"])) for video in new_video]
        await asyncio.wait(tasks)
    if len(new_video) == 1:
        buffer = BytesIO()
        buffer.write(tasks[0].result())
        buffer.seek(0)
        msg = await bot.send_photo(
            chat_id=config.main_chat,
            photo=buffer,
            caption=msg_text,
            reply_markup=markup
        )
    else:
        input_media = []
        for task in tasks:
            buffer = BytesIO()
            buffer.write(task.result())
            buffer.seek(0)
            input_media.append(InputMediaPhoto(buffer))
        input_media[0].caption = msg_text
        msg = await bot.send_media_group(
            chat_id=config.main_chat,
            media=MediaGroup(input_media),
        )
    await msg.pin()

