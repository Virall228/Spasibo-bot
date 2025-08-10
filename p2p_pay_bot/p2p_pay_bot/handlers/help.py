from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("📖 <b>Помощь:</b>

" +
                         "1. /new_request — создать запрос на оплату.
" +
                         "2. /market — список всех запросов.
" +
                         "3. /help — показать эту справку.")