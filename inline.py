from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import keteninurlsi
from config import darpaça
from config import slimfiturlsi
from config import regularfiturlsi
from config import oduncuurlsi
from config import regularurlsi

keten_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=keteninurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)

darpaça_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=darpaça),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)

slimfit_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=slimfiturlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)

regularfit_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=regularfiturlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)

oduncu_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=oduncuurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)

regular_URL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy here', url=regularurlsi),
            InlineKeyboardButton(text='Vazgeç', callback_data='cancel'),
        ]
    ],
    resize_keyboard = True,
    onetime_keyboard = True
)