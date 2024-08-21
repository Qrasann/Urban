from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
  print("Urban message")


@dp.message_handler()
async def all_message(message):
  print("Введите команду /start, чтобы начать общение.")


@dp.message_handler()
async def start(message):
  print("Привет! Я бот помогающий твоему здоровью.")


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
