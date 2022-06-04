from django.db import models


class ProductCategory(models.Model):
    class Status(models.TextChoices):
        active = 'active', 'Активный'
        deactive = 'deactive', 'Не активный'

    title = models.CharField(max_length=255,
                             verbose_name='Название',
                             unique=True)
    status = models.CharField(max_length=255,
                              verbose_name='Статус',
                              choices=Status.choices,
                              default=Status.active)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Status(models.TextChoices):
        active = 'active', 'Активный'
        deactive = 'deactive', 'Не активный'

    class UnitType(models.TextChoices):
        piece = 'piece', 'шт'
        kg = 'kg', 'кг'
        liter = 'liter', 'литр'

    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория',
                                 null=True)
    title = models.CharField(max_length=255,
                             verbose_name='Название')
    status = models.CharField(max_length=255,
                              verbose_name='Статус',
                              choices=Status.choices,
                              default=Status.active)
    unit = models.CharField(max_length=255,
                            verbose_name='Ед.изм',
                            choices=UnitType.choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductWeight(models.Model):
    weight = models.CharField(verbose_name='Вес', max_length=255)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.weight

    class Meta:
        verbose_name = 'Вес товара'
        verbose_name_plural = 'Весы товара'


class ProductColor(models.Model):
    color = models.CharField(max_length=200, verbose_name='Цвет')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цветы товара'
