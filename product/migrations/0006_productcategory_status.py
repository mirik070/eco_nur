# Generated by Django 3.2.13 on 2022-05-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220528_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='status',
            field=models.CharField(choices=[('active', 'Активный'), ('deactive', 'Не активный')], default='active', max_length=255, verbose_name='Статус'),
        ),
    ]
