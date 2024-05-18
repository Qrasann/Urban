#Задача «Работаем с выводом данных».
name_product = input("Введите название товара: ")
product_price = float(input("Введите стоимость товара: "))
product_weight = float(input("Введите вес товара: "))
customer_cash = float(input("Введите количество денег: "))

total_price = product_price * product_weight

customer_change = customer_cash - total_price

print(f"\nЧек: {name_product}, {product_weight}кг. {product_price} руб/кг. \nИтого: {total_price} руб. \nВнесено: {customer_cash} руб. \nСдача: {customer_change} руб")