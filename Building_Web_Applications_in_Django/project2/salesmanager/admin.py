from django.contrib import admin

from salesmanager.models import clients, items, sales

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=("name", "direction", "phone")
    search_fields=("name", "phone")

admin.site.register(clients, ClientAdmin)
admin.site.register(items)
admin.site.register(sales)