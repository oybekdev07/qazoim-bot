from aiogram import Router
from aiogram import types
from aiogram.filters import CommandStart
from keyboard import main_menu_keyboard
from texts import main_text

router = Router()

@router.message(CommandStart)
async def start_dispatcher(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(
        main_text.format(name=first_name),
        reply_markup=main_menu_keyboard,
    )
    