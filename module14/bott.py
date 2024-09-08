import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    keyboard.add(button_calculate, button_info)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = create_main_keyboard()
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Рассчитать')
def set_age(message):
    bot.send_message(message.chat.id, "Введите ваш возраст:")
    bot.register_next_step_handler(message, set_growth)

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

bot.polling()
