
from main import dp, bot
from aiogram.types import Message
from config import admin_id
from keyboard import magaza , kot_cesitleri, t_shirt_cesitleri, gömlek_cesitleri
from inline import keten_URL,darpaça_URL,slimfit_URL,regularfit_URL,oduncu_URL,regular_URL


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id,text='Bot is started')

@dp.message_handler()
async def speak(message: Message):
    if message.text.lower() == 'hello':
        await message.answer(f'Hello {message.from_user.first_name}')
    elif message.text == '/help':
        await message.answer('some /magaza function names and /menu')
    elif message.text == '/magaza':
        await message.answer('choose a type', reply_markup=magaza)
    elif message.text == 'kot':
        await message.answer (text='link', reply_markup=kot_cesitleri)
    elif message.text == 'keten':
        await message.answer (text='link', reply_markup=keten_URL)
    elif message.text == 'darpaça':
        await message.answer (text='link', reply_markup=darpaça_URL)
    elif message.text == 't-shirt':
        await message.answer (text='link', reply_markup=t_shirt_cesitleri)
    elif message.text == 'slimfit':
        await message.answer (text='link', reply_markup=slimfit_URL)
    elif message.text == 'regularfit':
        await message.answer (text='link', reply_markup=regularfit_URL)
    elif message.text == 'gomlek':
        await message.answer (text='link', reply_markup=gömlek_cesitleri)
    elif message.text == 'oduncu':
        await message.answer (text='link', reply_markup=oduncu_URL)
    elif message.text == 'regular':
        await message.answer (text='link', reply_markup=regular_URL)
