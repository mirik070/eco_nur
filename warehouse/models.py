from django.db import models

from user.models import User


class Raw(models.Model):
    class Status(models.TextChoices):
        active = 'active', 'Активный'
        deactive = 'deactive', 'Не активный'

    class UnitType(models.TextChoices):
        piece = 'piece', 'шт'
        kg = 'kg', 'кг'
        liter = 'liter', 'литр'

    title = models.CharField(max_length=255,
                             verbose_name='Название')
    unit = models.CharField(max_length=255,
                            verbose_name='Ед.изм',
                            choices=UnitType.choices)
    status = models.CharField(verbose_name='Статус',
                              max_length=255,
                              choices=Status.choices,
                              default=Status.active)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name='Цена', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сырье'
        verbose_name_plural = 'Сырье'


class WarehouseRaw(models.Model):
    raw = models.ForeignKey(Raw,
                            on_delete=models.CASCADE,
                            verbose_name='Сырье')
    count = models.FloatField(verbose_name='Кол-во')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.raw} | {self.count}"

    class Meta:
        verbose_name = 'Сырье в складе'
        verbose_name_plural = 'Сырье в складе'


class WarehouseProduct(models.Model):
    product = models.ForeignKey('product.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    product_color = models.ForeignKey('product.ProductColor',
                                      on_delete=models.CASCADE,
                                      verbose_name='Цвет товара',
                                      null=True)
    product_weight = models.ForeignKey('product.ProductWeight',
                                       on_delete=models.CASCADE,
                                       verbose_name='Вес/Размер товара',
                                       null=True)
    count = models.FloatField(verbose_name='Кол-во')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} | {self.count}"

    class Meta:
        verbose_name = 'Продукт в складе'
        verbose_name_plural = 'Продукты в складе'

