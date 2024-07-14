from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


@router.message(Command('Image'))
async def get_image(message: Message):
    await message.answer_photo(
        photo='https://quod.lib.umich.edu/f/fc/images/13761232.0043.102-00000001.jpg',
        caption='img1.jpg')
