from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text = 'Информация', callback_data='info')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
  keyword=[
    [KeyboardButton(text='Info')],
    [
      KeyboardButton(text='shop'),
      KeyboardButton(text='donate')
    ]
  ], resize_keyboard= True
)
@dp.message_handler(commands=['start'])
async def starter(message):
  await message.answer('Рады вас видеть!', reply_markup = start_menu)

#@dp.callback_query_handler(text = 'info')
#async def infor(call):
  #await call.message.anwer('Информация о боте')
  #await call.answer()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button)
kb.add(button2)

@dp.message_handler(command = ['start'])
async def start(message):
  await message.answer('Привет!', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform(message):
  await message.answer('Информация о боте!')


class UserState(StatesGroup):
  age = State()
  growth = State()
  weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
  await message.answer('Введите свой возраст:')
  await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
  await state.update_data(age=message.text)
  await message.answer('Введите свой рост:')
  await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
  await state.update_data(growth=message.text)
  await message.answer('Введите свой вес:')
  await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
  await state.update_data(weight=message.text)
  data = await state.get_data()

  age = int(data['age'])
  growth = int(data['growth'])
  weight = int(data['weight'])

  calories = 10 * weight + 6.25 * growth - 5 * age - 161

  await message.answer(f'Ваша норма калорий: {calories:.2f} ккал в день.')
  await state.finish()


@dp.message_handler(text=['/start', 'start'])
async def start(message: types.Message):
  await message.answer("Привет! Я бот, помогающий твоему здоровью. Нажмите 'Calories', чтобы начать.")


@dp.message_handler()
async def all_message(message: types.Message):
  await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)