from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7397323719:AAGK4BQLwKqQ3kK9H0gYxRo8-IRA9sMCs2U"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
  print("Urban message")


@dp.message_handler(text=['/start', 'start'])
async def start(message):
  print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def massages(message):
  print("Мы получили сообщение!")


@dp.message_handler()
async def all_massages(message):
  print("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
