from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Изображение')],
    [KeyboardButton(text='Ячейка А2'), KeyboardButton(text='Карта')],
    [KeyboardButton(text='Покупка')]
],      resize_keyboard=True,
        input_field_placeholder='Введите дату DD.MM.YYYY')
