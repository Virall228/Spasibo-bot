from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums.parse_mode import ParseMode

TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()