from aiogram import Router, types
from aiogram.filters import Command
from p2p_pay_bot.middleware.block import block_user, unblock_user, blocked_users

router = Router()

ADMIN_IDS = [123456789]  # замените на свой Telegram ID

@router.message(Command("block"))
async def block_command(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return await message.answer("❌ У вас нет прав.")

    try:
        user_id = int(message.text.split()[1])
        block_user(user_id)
        await message.answer(f"🚫 Пользователь {user_id} заблокирован.")
    except:
        await message.answer("⚠️ Используйте: /block <user_id>")

@router.message(Command("unblock"))
async def unblock_command(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return await message.answer("❌ У вас нет прав.")

    try:
        user_id = int(message.text.split()[1])
        unblock_user(user_id)
        await message.answer(f"✅ Пользователь {user_id} разблокирован.")
    except:
        await message.answer("⚠️ Используйте: /unblock <user_id>")

@router.message(Command("blocked"))
async def list_blocked(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return await message.answer("❌ У вас нет прав.")

    if not blocked_users:
        return await message.answer("✅ Никто не заблокирован.")

    await message.answer("🚫 Заблокированы:
" + "
".join(map(str, blocked_users)))