# Generated by Django 3.2.13 on 2022-04-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('shop_photo', models.ImageField(blank=True, null=True, upload_to='shop_photo/', verbose_name='Фото магазина')),
                ('shop_name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('accepted', 'Принято'), ('sent', 'Отправлено'), ('canceled', 'Отменено')], default='pending', max_length=255, verbose_name='Статус')),
                ('payment_type', models.CharField(choices=[('cash', 'Наличное'), ('enumeration', 'Перечисление')], max_length=255, verbose_name='Вид оплаты')),
                ('total', models.FloatField(verbose_name='Общая сумма')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='Кол-во')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Элемент заявки',
                'verbose_name_plural': 'Элементы заявки',
            },
        ),
    ]
