from django.contrib import admin
from .models import Status, Product, MyOrder, OrderLine

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date')
    inlines = (OrderLineInline, )

# Register your models here.
admin.site.register(Status)
admin.site.register(Product)
admin.site.register(MyOrder, OrderAdmin)
