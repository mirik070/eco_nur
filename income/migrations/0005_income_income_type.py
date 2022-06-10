# Generated by Django 3.2.13 on 2022-06-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_incomerawitem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='income_type',
            field=models.CharField(choices=[('income', 'Приход'), ('outcome', 'Расход')], default='income', max_length=255, verbose_name='Тип'),
        ),
    ]
