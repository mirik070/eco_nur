from django.contrib import admin

from product.models import Product, ProductWeight, ProductColor, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductWeight)
class ProductWeightAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    pass
