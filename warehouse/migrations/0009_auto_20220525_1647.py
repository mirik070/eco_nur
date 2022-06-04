# Generated by Django 3.2.13 on 2022-05-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20220525_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incomeproductitem',
            name='income',
        ),
        migrations.RemoveField(
            model_name='incomeproductitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='incomeproductitem',
            name='product_color',
        ),
        migrations.RemoveField(
            model_name='incomeproductitem',
            name='product_weight',
        ),
        migrations.RemoveField(
            model_name='incomerawitem',
            name='income',
        ),
        migrations.RemoveField(
            model_name='incomerawitem',
            name='raw',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='IncomeProductItem',
        ),
        migrations.DeleteModel(
            name='IncomeRawItem',
        ),
    ]
