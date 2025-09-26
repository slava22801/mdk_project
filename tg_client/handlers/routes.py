from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart

from keyboards.main_inlinekb import main_kb
from temp.data import data_dict

route = Router()

@route.message(CommandStart())
async def start_bot(message: Message):
    # kb = [
    #     [
    #         KeyboardButton(text="Купить тг звезды"),
    #         KeyboardButton(text="Купить аккаунт")
    #     ],
    # ]
    # keyboard = ReplyKeyboardMarkup(
    #     keyboard=kb,
    #     resize_keyboard=True,
    #     input_field_placeholder="Выберите действие"
    # )
    
    await message.answer("Приветствую вас в боте для приобретения цифровых товаров. Выберите ниже действие", reply_markup=main_kb(data_dict))



@route.message(F.text == "Купить тг звезды")
async def message_handler(message: Message):
    await message.answer("Покупка тг звезд", reply_markup=ReplyKeyboardRemove())