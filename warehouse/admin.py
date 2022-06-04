from django.contrib import admin

from warehouse.models import Raw, WarehouseRaw, WarehouseProduct


@admin.register(Raw)
class RawAdmin(admin.ModelAdmin):
    pass


@admin.register(WarehouseRaw)
class WarehouseRawAdmin(admin.ModelAdmin):
    pass


@admin.register(WarehouseProduct)
class WarehouseProductAdmin(admin.ModelAdmin):
    pass
