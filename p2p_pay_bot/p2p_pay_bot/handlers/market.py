from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from p2p_pay_bot.handlers.new_request import requests

router = Router()

@router.message(commands=["market"])
async def cmd_market(message: types.Message):
    if not requests:
        return await message.answer("📭 Пока нет активных запросов.")

    for i, req in enumerate(requests):
        if req.get("taken_by"):
            continue  # скрываем уже взятые заявки
        builder = InlineKeyboardBuilder()
        builder.button(
            text="💸 Оплатить заявку",
            callback_data=f"accept_{i}"
        )
        user = f"@{req['username']}" if req["username"] else f"ID {req['user_id']}"
        text = (f"<b>{req['title']}</b>
"
                f"💶 Сумма: €{req['amount']}
"
                f"👤 Пользователь: {user}
"
                f"🔗 TON кошелёк: <code>{req['wallet']}</code>")
        await message.answer(text, reply_markup=builder.as_markup())