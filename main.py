from aiogram import Bot, Dispatcher
from handlers.content import db
from handlers.command import router
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(db)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
