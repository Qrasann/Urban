from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils import run_polling
from aiogram.fsm.storage.memory import MemoryStorage

api = "7058673152:AAFnRsfr2X0MeuHJAxIev_bxUWcKy60-ck0"
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет!")

if __name__ == '__main__':
    run_polling(dp, skip_updates=True)
