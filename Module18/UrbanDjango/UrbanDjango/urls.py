from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from task4.views import main_view, shop_view, cart_view

urlpatterns = [
    path('', lambda request: redirect('menu')),  # Редирект с пустого пути на /main/
    path('menu/', main_view, name='menu'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),  # Подключаем маршруты task2
]
