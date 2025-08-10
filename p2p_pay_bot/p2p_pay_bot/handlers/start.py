from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("👋 Добро пожаловать в P2P Pay Bot!

" +
                         "💡 Здесь вы можете создать запрос на оплату или помочь другим.
" +
                         "Используйте команды:
" +
                         "/new_request - создать запрос
" +
                         "/market - посмотреть активные запросы
" +
                         "/help - помощь")