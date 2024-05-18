#Задача «Сдача всем».
price = float(input("Введите стоимость товара: "))
weight = float(input("Введите вес товара: "))
cash = float(input("Введите количество денег: "))

sum = price * weight

change = cash - sum
print(f"Ваша сдача: {change}")