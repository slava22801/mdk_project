from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from temp.data import data_dict

def main_kb(data_dict: dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for data_id, data_name in data_dict.items():
        builder.row(
            InlineKeyboardButton(
                text=data_name.get('name'),
                callback_data=f'name_{data_id}'
            )
        )
    # Добавляем кнопку "На главную"
    builder.row(
        InlineKeyboardButton(
            text='На главную',
            callback_data='back_home'
        )
    )
    # Настраиваем размер клавиатуры
    builder.adjust(1)
    return builder.as_markup()