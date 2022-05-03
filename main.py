import os

os.chdir(
    os.path.abspath(
        os.path.dirname(__file__)
    )
)

import handlers

from aiogram import executor
from config import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from schedulers import *

async def on_startup(dp):
    scheduler.start()

async def on_shutdown(dp):
    scheduler.shutdown(wait=False)

scheduler = AsyncIOScheduler()
scheduler.add_job(yt_notify_video, "interval", minutes=config.update_interval)

if __name__ == "__main__":
    from dispatcher import dp

    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )

