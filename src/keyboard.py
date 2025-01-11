from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.texts import *

main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=forget_prayer_btn_text, callback_data="forget_prayer_main_command"),
            InlineKeyboardButton(text=prayer_btn_text, callback_data="prayer_time_main_command"),
        ],
        [
            InlineKeyboardButton(text=about_bot_btn_text, callback_data="about_bot_main_command"),
        ],
    ]
)


bot_about_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=how_to_use_bot, callback_data="how_to_use_bot_command"),
        ],
        [
            InlineKeyboardButton(text=faq_btn_text, callback_data="faq_main_command"),
        ],
        [
            InlineKeyboardButton(text=go_back_btn_text, callback_data="main_menu"),
        ],
    ]
)


def go_back_keyboard(command):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=go_back_btn_text, callback_data=command)],
    ])


def regions_keyboard():
    # 2 qatorlik bo'lishi uchun har ikkita elementni bir guruhga ajratamiz
    keyboard = [
        [
            InlineKeyboardButton(text=regions[i]["name"], callback_data=regions[i]["callback"]),
            InlineKeyboardButton(text=regions[i + 1]["name"], callback_data=regions[i + 1]["callback"])
        ]
        for i in range(0, len(regions) - 1, 2)  # 2 qadam bilan o'rnatish
    ]

    # Agar regionlar soni toq bo'lsa, oxirgi elementni alohida qo'shamiz
    if len(regions) % 2 != 0:
        keyboard.append([InlineKeyboardButton(text=regions[-1]["name"], callback_data=regions[-1]["callback"])])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def district_keyboard(region_name):
    # 2 qatorlik bo'lishi uchun har ikkita elementni bir guruhga ajratamiz
    district_list = []
    for region in regions:
        if region['callback'] == region_name:
            district_list = region['districts']
            region_clicked_name = region['name']
    if district_list:
        keyboard = [
            [
                InlineKeyboardButton(text=district_list[i]["name"], callback_data=district_list[i]["callback"]),
                InlineKeyboardButton(text=district_list[i + 1]["name"], callback_data=district_list[i + 1]["callback"])
            ]
            for i in range(0, len(district_list) - 1, 2)  # 2 qadam bilan o'rnatish
        ]

        # Agar regionlar soni toq bo'lsa, oxirgi elementni alohida qo'shamiz
        if len(district_list) % 2 != 0:
            keyboard.append([InlineKeyboardButton(text=district_list[-1]["name"], callback_data=district_list[-1]["callback"])])
            
        keyboard.append([InlineKeyboardButton(text=go_back_btn_text, callback_data="prayer_time_main_command")])
        return region_clicked_name, InlineKeyboardMarkup(inline_keyboard=keyboard)
    return False, False
    
