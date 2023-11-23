from django.contrib import admin

from products.models import Item


# Register your models here.


@admin.register(Item)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency', )
    list_filter = ('price', 'currency', )
    search_fields = ('name', 'price', )
