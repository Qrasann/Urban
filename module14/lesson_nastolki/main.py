from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispactcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup = start_kb)

@dp.message_handler(texts = 'Стоимость')
async def price(message):
    await message.anwer(texts.about, reply_markup = start_kb)

@dp.message_handler(texts = 'О нас')
async def info(message):
    await message.answer(reply_markup = catalog_kb)

api= ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())











if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

