from django.db import models

from user.models import User


class Order(models.Model):
    class Status(models.TextChoices):
        created = 'created', 'Создано'
        pending = 'pending', 'В ожидании'
        accepted = 'accepted', 'Принято'
        sent = 'sent', 'Отправлено'
        canceled = 'canceled', 'Отменено'

    class PaymentType(models.TextChoices):
        cash = 'cash', 'Наличное'
        enumeration = 'enumeration', 'Перечисление'

    agent = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='Агент')
    address = models.CharField(max_length=255,
                               verbose_name='Адрес')
    shop_photo = models.ImageField(verbose_name='Фото магазина', upload_to='shop_photo/', blank=True, null=True)
    shop_name = models.CharField(max_length=255,
                                 verbose_name='Название магазина')
    phone = models.CharField(max_length=255,
                             verbose_name='Номер телефона')
    status = models.CharField(max_length=255,
                              verbose_name='Статус',
                              choices=Status.choices,
                              default=Status.created)
    payment_type = models.CharField(max_length=255,
                                    verbose_name='Вид оплаты',
                                    choices=PaymentType.choices)
    total = models.FloatField(verbose_name='Общая сумма', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.agent} | {self.address} | {self.total}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name='Заявка')
    product = models.ForeignKey('product.Product',
                                on_delete=models.PROTECT,
                                verbose_name='Продукт', null=True)
    product_color = models.ForeignKey('product.ProductColor',
                                      on_delete=models.PROTECT,
                                      verbose_name='Цвет товара', null=True)
    product_weight = models.ForeignKey('product.ProductWeight',
                                       on_delete=models.PROTECT,
                                       verbose_name='Вес товара', null=True)
    count = models.FloatField(verbose_name='Кол-во')
    content = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.count}'

    class Meta:
        verbose_name = 'Элемент заявки'
        verbose_name_plural = 'Элементы заявки'
