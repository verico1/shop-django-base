# Generated by Django 3.1.5 on 2021-03-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_auto_20210315_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='quantity'),
        ),
    ]