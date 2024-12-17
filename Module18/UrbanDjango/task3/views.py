from django.shortcuts import render

def main_view(request):
    return render(request, 'fourth_task/menu.html')

def shop_view(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
    return render(request, 'fourth_task/shop.html', context)

def cart_view(request):
    return render(request, 'fourth_task/cart.html')
