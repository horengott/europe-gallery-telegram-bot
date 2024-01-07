import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os

# logging
logging.basicConfig(level=logging.INFO)

# bot
load_dotenv()
bot = Bot(os.getenv("TOKEN"))

# dispatcher
dp = Dispatcher()

# handlers - commands
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"{message.from_user.first_name}, wellcome to the best gallery of the pics of europe!")

@dp.message()
async def answer(message: types.Message):
    await message.reply("i´m sorry, i don´t understand :(")    

# polling
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())