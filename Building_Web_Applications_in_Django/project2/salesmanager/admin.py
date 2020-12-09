from django.contrib import admin

from salesmanager.models import clients, items, sales

# Register your models here.

admin.site.register(clients)
admin.site.register(items)
admin.site.register(sales)