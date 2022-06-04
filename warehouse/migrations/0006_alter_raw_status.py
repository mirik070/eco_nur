# Generated by Django 3.2.13 on 2022-05-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_auto_20220522_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw',
            name='status',
            field=models.CharField(choices=[('created', 'Создано'), ('ready', 'На складе'), ('finished', 'Закончен')], default='ready', max_length=255, verbose_name='Статус'),
        ),
    ]
