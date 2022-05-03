from aiogram import Bot, Dispatcher
from config import config
from filters import bound_filters

bot = Bot(
    token=config.token,
    parse_mode="HTML"
)
dp = Dispatcher(bot)

for flt in bound_filters:
    dp.filters_factory.bind(flt)

