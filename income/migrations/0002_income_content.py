# Generated by Django 3.2.13 on 2022-05-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
    ]
