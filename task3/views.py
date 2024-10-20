from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'game1': 'Minecraft',
        'game2': 'Sekiro: Shadow die twice',
        'game3': 'Dark Souls',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
