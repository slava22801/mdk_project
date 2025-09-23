from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

route = Router(name=__name__)


@route.message()
async def message_handler(message: Message):
    await message.dice()