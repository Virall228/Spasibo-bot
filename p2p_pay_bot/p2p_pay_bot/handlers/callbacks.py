from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from p2p_pay_bot.handlers.new_request import requests
from p2p_pay_bot.middleware.block import is_blocked

router = Router()

@router.callback_query(lambda c: c.data.startswith("accept_"))
async def accept_request(callback: types.CallbackQuery):
    if is_blocked(callback.from_user.id):
        return await callback.message.answer("🚫 Вы заблокированы и не можете выполнять заявки.")

    index = int(callback.data.split("_")[1])
    req = requests[index]

    if req.get("taken_by"):
        return await callback.answer("❌ Заявка уже выполняется.", show_alert=True)

    req["taken_by"] = callback.from_user.id
    await callback.message.edit_text(
        callback.message.text + f"

✅ В процессе: @{callback.from_user.username or callback.from_user.id}"
    )
    await callback.answer("🔄 Вы приняли заявку. Свяжитесь с автором для деталей.")