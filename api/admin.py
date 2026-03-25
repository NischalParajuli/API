from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id','name')

class FoodAdmin(admin.ModelAdmin):
   list_display = ('name','price','category')
   list_filter = ('category',)
   search_fields = ('name',)
   list_per_page = 15
admin.site.register(Food, FoodAdmin)

class TableAdmin(admin.ModelAdmin):
   list_display = ('number','is_available')
   list_filter = ('is_available',)
   list_editable = ('is_available',)
admin.site.register(Table, TableAdmin)

class OrderItemInline(admin.TabularInline):
   model = OrderItem
   autocomplete_fields = ('food',)
   extra = 0

class OrderAdmin(admin.ModelAdmin):
   list_display = ('id','user','total_price','status')
   search_fields = ('user',)
   list_filter = ('status',)
   list_editable = ('status',)
   inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
   list_display = ('id','order','food')
admin.site.register(OrderItem,OrderItemAdmin)