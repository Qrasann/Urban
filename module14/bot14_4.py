import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products
from crud_functions import add_product
import os

if os.path.exists('products.db'):
    os.remove('products.db')

initiate_db()

add_product("Apple", "Fresh red apple", 50, 'https://i.pinimg.com/564x/57/c3/f2/57c3f2c3037afad432a93ab72aa23066.jpg')
add_product("Banana", "Sweet banana", 30, 'https://i.pinimg.com/564x/35/56/5b/35565b8ab6786d88734f566f3d785c18.jpg')
add_product("Orange", "Juicy orange", 40, 'https://i.pinimg.com/736x/51/76/e2/5176e2e23cf66beaed7ce63454e3344f.jpg')
add_product("Milk", "Fresh milk", 60, 'https://i.pinimg.com/564x/71/9d/3b/719d3b626babfebadb6207bb652d1bae.jpg')


API_TOKEN = '7397323719:AAGK4BQLwKqQ3kK9H0gYxRo8-IRA9sMCs2U'
bot = telebot.TeleBot(API_TOKEN)

initiate_db()

def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    button_buy = KeyboardButton('Купить')
    keyboard.add(button_calculate, button_info)
    keyboard.add(button_buy)
    return keyboard

def create_product_keyboard():
    keyboard = InlineKeyboardMarkup()
    products = get_all_products()
    for product in products:
        button = InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}')
        keyboard.add(button)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = create_main_keyboard()
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Рассчитать')
def main_menu(message):
  keyboard = create_main_keyboard()
  bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'formulas')
def get_formulas(call):
  formula_message = (
    "Формула Миффлина-Сан Жеора:\n"
    "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n"
    "Для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) - 161"
  )
  bot.send_message(call.message.chat.id, formula_message)


@bot.callback_query_handler(func=lambda call: call.data == 'calories')
def set_age(call):
  bot.send_message(call.message.chat.id, "Введите ваш возраст:")
  bot.register_next_step_handler(call.message, set_growth)


def set_growth(message):
  try:
    age = int(message.text)
    bot.send_message(message.chat.id, "Введите ваш рост в см:")
    bot.register_next_step_handler(message, set_weight, age)
  except ValueError:
    bot.send_message(message.chat.id, "Пожалуйста, введите корректный возраст.")
    bot.register_next_step_handler(message, set_age)


def set_weight(message, age):
  try:
    growth = int(message.text)
    bot.send_message(message.chat.id, "Введите ваш вес в кг:")
    bot.register_next_step_handler(message, calculate_calories, age, growth)
  except ValueError:
    bot.send_message(message.chat.id, "Пожалуйста, введите корректный рост.")
    bot.register_next_step_handler(message, set_growth)


def calculate_calories(message, age, growth):
  try:
    weight = int(message.text)
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    bot.send_message(message.chat.id, f"Ваша базальная метаболическая скорость (BMR): {bmr} калорий в день.")
  except ValueError:
    bot.send_message(message.chat.id, "Пожалуйста, введите корректный вес.")
    bot.register_next_step_handler(message, set_weight, age, growth)


@bot.message_handler(func=lambda message: message.text == 'Информация')
def info(message):
  bot.send_message(message.chat.id, "Это бот для расчета нормы калорий по параметрам тела.")

@bot.message_handler(func=lambda message: message.text == 'Купить')
def get_buying_list(message):
    products = get_all_products()
    for product in products:
        response = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
        if product[4]:
            response += f"\nИзображение: {product[4]}"
        bot.send_message(message.chat.id, response)
    keyboard = create_product_keyboard()
    bot.send_message(message.chat.id, "Выберите продукт для покупки:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('product_'))
def send_confirm_message(call):
    product_id = call.data.split('_')[1]
    bot.send_message(call.message.chat.id, f"Вы успешно приобрели продукт с ID: {product_id}!")



bot.polling()
