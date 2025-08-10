import asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from p2p_pay_bot.bot import bot, dp
from p2p_pay_bot.handlers import start, help, new_request, market, admin, callbacks

async def main():
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(new_request.router)
    dp.include_router(market.router)
    dp.include_router(callbacks.router)
    dp.include_router(admin.router)
    dp.storage = MemoryStorage()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())