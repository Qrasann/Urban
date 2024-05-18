#Задача «Сложная сдача».
cash = int(input("Введите ваш баланс: "))

price = 34
weight = 4.5

sum = price * weight

change = cash - sum

print(f"Ваша сдача: {change}")