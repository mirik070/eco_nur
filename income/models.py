from django.db import models


class Income(models.Model):
    class Status(models.TextChoices):
        created = 'created', 'Создано'
        accepted = 'accepted', 'Принято'
        canceled = 'canceled', 'Отменено'

    class Warehouse(models.TextChoices):
        product = 'product', 'Продуктовый'
        raw = 'raw', 'Сырьевой'

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE,
                             verbose_name='Юзер')
    total = models.FloatField(verbose_name='Общяя сумма', default=0)
    status = models.CharField(choices=Status.choices,
                              verbose_name='Статус',
                              max_length=255,
                              default=Status.created)
    warehouse_type = models.CharField(max_length=255,
                                      verbose_name='Тип склада',
                                      choices=Warehouse.choices)
    content = models.TextField(verbose_name='Контент', null=True, blank=True)

    def __str__(self):
        return f'{self.created_at}'

    class Meta:
        verbose_name = 'Приход'
        verbose_name_plural = 'Приходы'


class IncomeProductItem(models.Model):
    product = models.ForeignKey('product.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Продукт')
    product_color = models.ForeignKey('product.ProductColor',
                                      on_delete=models.CASCADE,
                                      verbose_name='Цвет товара',
                                      null=True)
    product_weight = models.ForeignKey('product.ProductWeight',
                                       on_delete=models.CASCADE,
                                       verbose_name='Вес/Размер товара',
                                       null=True)
    income = models.ForeignKey(Income,
                               on_delete=models.CASCADE,
                               verbose_name='Приход')
    count = models.FloatField(verbose_name='Кол-во')
    price = models.FloatField(verbose_name='Цена')
    total = models.FloatField(verbose_name='Общая сумма')
    content = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.product.title}'

    class Meta:
        verbose_name = 'Приход продукции'
        verbose_name_plural = 'Приходы продукции'


class IncomeRawItem(models.Model):
    raw = models.ForeignKey('warehouse.Raw',
                            on_delete=models.CASCADE,
                            verbose_name='Сырье')
    income = models.ForeignKey(Income,
                               on_delete=models.CASCADE,
                               verbose_name='Приход')
    count = models.FloatField(verbose_name='Кол-во')
    price = models.FloatField(verbose_name='Цена')
    total = models.FloatField(verbose_name='Общая сумма')
    content = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return self.raw.title

    class Meta:
        verbose_name = 'Приход сырья'
        verbose_name_plural = 'Приходы сырья'
