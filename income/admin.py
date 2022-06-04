from django.contrib import admin

from income.models import Income, IncomeProductItem, IncomeRawItem


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass


@admin.register(IncomeProductItem)
class IncomeProductItemAdmin(admin.ModelAdmin):
    pass


@admin.register(IncomeRawItem)
class IncomeRawItemAdmin(admin.ModelAdmin):
    pass
