import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🍾 KissUZ ga xush kelibsiz!\n"
        "Do‘stlaringiz bilan o‘yinni boshlang!"
    )


async def index(request):
    return web.Response(text="KissUZ server ishlayapti!")


async def health(request):
    return web.json_response({"status": "ok"})


async def on_startup(app):
    app["bot_task"] = asyncio.create_task(dp.start_polling(bot))


async def on_cleanup(app):
    app["bot_task"].cancel()
    await bot.session.close()


app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/api/health", health)
app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN kiritilmagan!")

    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
