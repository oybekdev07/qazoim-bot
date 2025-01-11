from aiogram import Router
from aiogram.types import CallbackQuery
from .functions import get_prayer_time
from .command import *
from keyboard import *
from datetime import datetime
db = Router()

    
@db.callback_query(lambda query: query.data == "faq_main_command")
async def faq_dispatcher(query: CallbackQuery):
    await query.message.edit_text(
        text=faq_main_text,
        reply_markup=go_back_keyboard("main_menu"),
    )


@db.callback_query(lambda query: query.data == "forget_prayer_main_command")
async def forget_prayer_dispatcher(query):
    await query.message.edit_text(
        text=forget_prayer_text,
        reply_markup=go_back_keyboard("main_menu"),

    )


@db.callback_query(lambda query: query.data == "main_menu")
async def go_to_main_menu_dispatcher(query):
    first_name = query.from_user.first_name
    await query.message.edit_text(
        text=main_text.format(name=first_name),
        reply_markup=main_menu_keyboard,
    )


@db.callback_query(lambda query: query.data == "prayer_time_main_command")
async def prayer_time_dispatcher(query):
    await query.message.edit_text(
        text=prayer_time_region_text,
        reply_markup=regions_keyboard(),
    )


@db.callback_query(lambda query: query.data == "about_bot_main_command")
async def prayer_time_dispatcher(query):
    await query.message.edit_text(
        text=about_bot_text,
        reply_markup=bot_about_keyboard,
    )



@db.callback_query(lambda query: query.data.startswith("region_"))
async def prayer_time_dispatcher(query):
    region_name, keyboard = district_keyboard(query.data)
    if keyboard:
        return await query.message.edit_text(
            text=prayer_time_districts_text.format(region_name=region_name),
            reply_markup=keyboard
        )
    await query.answer(something_went_wrong)
    

@db.callback_query(lambda query: query.data.startswith("city_"))
async def prayer_time_dispatcher(query):
    clicked_query = query.data
    city_name = clicked_query.split("_")[1]
    fajr, shuhr, dhuhr, asr, maghrib, isha = get_prayer_time.get_prayer_times(city_name)
    if fajr:
        today = datetime.now().date()
        return await query.message.edit_text(
            text=prayer_time_text.format(date=today,fajr=fajr,shuhr=shuhr,dhuhr=dhuhr,asr=asr,maghrib=maghrib,isha=isha),
            reply_markup=go_back_keyboard("prayer_time_main_command")
        )
    await query.answer(something_went_wrong)

