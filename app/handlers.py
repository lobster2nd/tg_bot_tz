from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.google_sheets.google_sheets import get_cell_value

from dotenv import load_dotenv
load_dotenv()

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


@router.message(Command('Image'))
async def get_image(message: Message):
    await message.answer_photo(
        photo='https://quod.lib.umich.edu/f/fc/images/13761232.0043.102-00000001.jpg',
        caption='img1.jpg')


@router.message(Command('GetCell'))
async def get_cell(message: Message, cell_value='A2'):
    value = get_cell_value(cell_value)
    await message.answer(f'Значение ячейки: {value}')
