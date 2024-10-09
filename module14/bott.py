import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

def create_inline_keyboard():
    keyboard = InlineKeyboardMarkup()
    button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    keyboard.add(button_calories, button_formulas)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = telebot.types.KeyboardButton('Рассчитать')
    button_info = telebot.types.KeyboardButton('Информация')
    keyboard.add(button_calculate, button_info)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Рассчитать')
def main_menu(message):
    keyboard = create_inline_keyboard()
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'formulas')
def get_formulas(call):
    formula_message = "Формула Миффлина-Сан Жеора:\n" \
                      "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n" \
                      "Для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) - 161"
    bot.send_message(call.message.chat.id, formula_message)

@bot.callback_query_handler(func=lambda call: call.data == 'calories')
def set_age(call):
    bot.send_message(call.message.chat.id, "Введите ваш возраст:")

bot.polling()
