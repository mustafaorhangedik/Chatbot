from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


magaza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='kot'),
            KeyboardButton(text='t-shirt')
        ],
        [
            KeyboardButton(text='gomlek')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

kot_cesitleri = ReplyKeyboardMarkup(
    keyboard =[
        [
            KeyboardButton(text='keten'),
            KeyboardButton(text='darpaça'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

t_shirt_cesitleri = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='slimfit'),
            KeyboardButton(text='regularfit'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

gömlek_cesitleri = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='oduncu'),
            KeyboardButton(text='regular'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)