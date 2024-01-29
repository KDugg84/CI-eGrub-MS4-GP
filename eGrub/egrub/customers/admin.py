from django.contrib import admin
from .models import MenuItems, Category, OrderModel


admin.site.register(MenuItems)
admin.site.register(Category)
admin.site.register(OrderModel)