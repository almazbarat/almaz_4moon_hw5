# Generated by Django 4.1 on 2022-08-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
