from config import bot_token
import asyncio
from aiogram import Bot, Dispatcher, executor
bot = Bot(bot_token, parse_mode='HTML')
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
