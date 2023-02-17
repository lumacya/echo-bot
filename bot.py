import time
import logging
from secret import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    logging.info(f'{user_id=} {user_full_name=}', time.asctime())

    await message.reply(f"Welcome to my first telegram bot, {user_full_name}!")

@dp.message_handler(commands=['help'])
async def help_handler():

    await f'I can echo your messages. Try me!'


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
