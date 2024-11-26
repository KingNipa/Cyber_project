from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','created_at')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'ordered_at')
    search_fields = ('user__username', 'product__name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
