# Generated by Django 3.2.13 on 2022-05-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderitem_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0, verbose_name='Общая сумма'),
        ),
    ]
