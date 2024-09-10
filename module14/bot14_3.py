import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)


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
  button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
  button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
  button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
  button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
  keyboard.add(button1, button2)
  keyboard.add(button3, button4)
  return keyboard


@bot.message_handler(commands=['start'])
def start(message):
  keyboard = create_main_keyboard()
  bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Рассчитать')
def main_menu(message):
  keyboard = create_inline_keyboard()
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
  products = [
    {'name': 'Product1', 'description': 'Описание 1', 'price': 100, 'image_url': 'https://i.pinimg.com/564x/57/c3/f2/57c3f2c3037afad432a93ab72aa23066.jpg'},
    {'name': 'Product2', 'description': 'Описание 2', 'price': 200, 'image_url': 'https://i.pinimg.com/564x/35/56/5b/35565b8ab6786d88734f566f3d785c18.jpg'},
    {'name': 'Product3', 'description': 'Описание 3', 'price': 300, 'image_url': 'https://i.pinimg.com/736x/51/76/e2/5176e2e23cf66beaed7ce63454e3344f.jpg'},
    {'name': 'Product4', 'description': 'Описание 4', 'price': 400, 'image_url': 'https://i.pinimg.com/564x/71/9d/3b/719d3b626babfebadb6207bb652d1bae.jpg'},
  ]

  for product in products:
    bot.send_message(message.chat.id,f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}")
    bot.send_photo(message.chat.id, product['image_url'])

  keyboard = create_product_keyboard()
  bot.send_message(message.chat.id, "Выберите продукт для покупки:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'product_buying')
def send_confirm_message(call):
  bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")


bot.polling()
