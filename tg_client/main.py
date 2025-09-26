import asyncio
import logging
import sys
from os import getenv


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers.routes import route

BOT_TOKEN = "8336673216:AAHsi0V_uinUMyGm-8yogM74ybLdJ09xGI8"


dp = Dispatcher()
dp.include_router(router=route)

async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())