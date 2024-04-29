# -*- coding: utf-8 -*-

# Блоки кода
x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат:', z)

# Ср. с C++
# if (x < 0) { printf('Меньше нуля\n');z=x**2+y;}else{printf('Больше нуля\n');z = x - y;}printf('Получается\n',z)

# Вложенные блоки кода
name = input('Введите ваше имя >>> ')
if name == 'Ola':
    opponent = 'Ola'
    print('Привет, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Привет, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Привет, Katy!')
        else:
            opponent = 'anonymous'
            print('Привет, anonymous!')

# Оператор pass
if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# Соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в Python
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа
if x < 0:
    if y > 0:
        pass  # Оператор pass используется, когда нужно указать блок кода, но в нем нет действий.
    else:
        print('Направо!')
else:
    print('Стой!')

# Максимальная длина строки
my_poem = [
    'Варкалось, хливкие шорьки пырялись по наве',
    'И хрюкотали зелюки как мюмзики в мове',
    'О бойся Бармаглота, сын! Он так свирлеп и дик',
    'А в глуше рымит исполин - Злопастный Брандашмыг!',
]

# Пробелы в операторах
x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6]

# reformat кода

x = 3

if x == 3:
    print(42)

if x < 0:
    print('Направо!')
else:
    print('Стой!')

# Названия переменных
number_of_my_pets = 34  # Переименование переменной в соответствии с PEP8
if number_of_my_pets > 10:
    print('Мне нужно больше места для моих питомцев!')

favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
if 'lion' in favorite_pets_and_bird:
    print('Вау!')

FavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']  # Стиль CamelCase для названия класса

# Рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать такие однобуквенные имена только для:
#   i j k - для циклов
#   x y z - для координат

# Никогда не используйте в названиях переменных одиночные l, I, O !
num_l = 34
num_I = 43
if num_l > num_I:
    print()
num_O = 9
if num_O > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

ss = ['cat', 'wolf', 'ostrich']
if 'lion' in ss:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
