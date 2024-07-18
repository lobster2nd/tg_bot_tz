from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.google_sheets.google_sheets import get_cell_value, write_cell_value
from app.maps.maps import generate_location_link

from dotenv import load_dotenv

import app.keyboards as kb

load_dotenv()

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}\n'
                         f'Введите дату в формате DD.MM.YYYY',
                         reply_markup=kb.main)


@router.message(F.text == 'Изображение')
async def get_image(message: Message):
    await message.answer_photo(
        photo='https://quod.lib.umich.edu/f/fc/images/13761232.0043.102-00000001.jpg',
        caption='img1.jpg')


@router.message(F.text == 'Ячейка А2')
async def get_cell(message: Message, cell_value='A2'):
    value = get_cell_value(cell_value)
    await message.answer(f'Значение ячейки: {value}')


@router.message(F.text == 'Карта')
async def get_location(message: Message, place='улица Ленина 1, Москва'):
    await message.answer(generate_location_link(place))


@router.message(F.text)
async def write_cell(message: Message):
    result = write_cell_value(message.text)
    await message.answer(result)

