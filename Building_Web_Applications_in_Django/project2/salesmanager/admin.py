from django.contrib import admin

from salesmanager.models import clients, items, sales

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=("name", "direction", "phone")
    search_fields=("name", "phone")

class ItemsAdmin(admin.ModelAdmin):
    list_filter=("section",)

class SalesAdmin(admin.ModelAdmin):
    list_display=("number","date")
    list_filter=("date",)
    date_hierarchy="date"

admin.site.register(clients, ClientAdmin)
admin.site.register(items, ItemsAdmin)
admin.site.register(sales, SalesAdmin)