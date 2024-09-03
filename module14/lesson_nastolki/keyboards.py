from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard =(
        [InlineKeyboardButton(text='Med size game', callback_data='medium')],
        [InlineKeyboardButton(text='Big size game', callback_data='big')],
        [InlineKeyboardButton(text='Very big size game', callback_data='VeryBig')],
        [InlineKeyboardButton(text='Other games', callback_data='other'],
    )
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Order', url = '#')],
        [InlineKeyboardButton(text='Back', callback_data='back_to_catalog')]
    ]
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Users',callback_data='users')],
        [InlineKeyboardButton(text='Statistics', callback_data='stats')],
        [
         InlineKeyboardButton(text='Block', callback_data='block')
         InlineKeyboardButton(text='Unblock', callback_data='unblock')



        ]
    ]
)









