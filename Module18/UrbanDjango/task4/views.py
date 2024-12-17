from django.shortcuts import render


def main_view(request):
  return render(request, 'fourth_task/menu.html')


def shop_view(request):
  # Статические данные товаров
  products = [
    {'name': 'Atomic Heart', 'price': 50},
    {'name': 'Cyberpunk 2077', 'price': 60},
    {'name': 'Doom Eternal', 'price': 40}
  ]
  return render(request, 'fourth_task/shop.html', {'products': products})


def cart_view(request):
  cart_items = [
    {'id': 1, 'name': 'Atomic Heart', 'price': 50},
    {'id': 2, 'name': 'Cyberpunk 2077', 'price': 60}
  ]

  total_cost = sum(item['price'] for item in cart_items)

  context = {
    'cart_items': cart_items,
    'total_cost': total_cost
  }

  return render(request, 'fourth_task/cart.html', context)
