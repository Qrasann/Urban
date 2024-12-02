import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from transitions import Machine
from crud_functions import initiate_db, add_user, is_included

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

# Определяем состояния для машины состояний
class RegistrationState:
    username = 'username'
    email = 'email'
    age = 'age'
    balance = 1000

# Определяем класс состояния для регистрации
class RegistrationMachine(Machine):
    def __init__(self, bot, user_id):
        self.bot = bot
        self.user_id = user_id
        self.state = None
        self.username = None
        self.email = None
        self.age = None
        super().__init__(initial='start', states=['start', RegistrationState.username, RegistrationState.email, RegistrationState.age], transitions=[
            {'trigger': 'next', 'source': 'start', 'dest': RegistrationState.username},
            {'trigger': 'next', 'source': RegistrationState.username, 'dest': RegistrationState.email},
            {'trigger': 'next', 'source': RegistrationState.email, 'dest': RegistrationState.age},
            {'trigger': 'finish', 'source': RegistrationState.age, 'dest': 'start'}
        ])

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_age(self, age):
        self.age = age
        add_user(self.username, self.email, self.age)

# Основной бот инициализация
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_register = KeyboardButton('Регистрация')
    keyboard.add(button_register)
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    initiate_db()  # Инициализация базы данных
    keyboard = create_main_keyboard()
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Регистрация')
def sing_up(message):
    registration_machine = RegistrationMachine(bot, message.chat.id)
    registration_machine.next()
    bot.send_message(message.chat.id, "Введите имя пользователя (только латинский алфавит):")
    bot.register_next_step_handler(message, set_username, registration_machine)

def set_username(message, registration_machine):
    username = message.text
    if is_included(username):
        bot.send_message(message.chat.id, "Пользователь существует, введите другое имя.")
        bot.register_next_step_handler(message, set_username, registration_machine)
    else:
        registration_machine.set_username(username)
        registration_machine.next()
        bot.send_message(message.chat.id, "Введите свой email:")
        bot.register_next_step_handler(message, set_email, registration_machine)

def set_email(message, registration_machine):
    registration_machine.set_email(message.text)
    registration_machine.next()
    bot.send_message(message.chat.id, "Введите свой возраст:")
    bot.register_next_step_handler(message, set_age, registration_machine)

def set_age(message, registration_machine):
    try:
        registration_machine.set_age(int(message.text))
        bot.send_message(message.chat.id, "Регистрация прошла успешно!")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный возраст.")
        bot.register_next_step_handler(message, set_age, registration_machine)

bot.polling()
