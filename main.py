from aiohttp import web
from aiogram import Bot, Dispatcher
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    print("KissUZ bot ishga tushdi!")

if __name__ == "__main__":
    asyncio.run(main())