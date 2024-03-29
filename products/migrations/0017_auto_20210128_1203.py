# Generated by Django 3.1.5 on 2021-01-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210128_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_brand',
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.ManyToManyField(default='', null=True, to='products.Brand', verbose_name='brand'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(default='', null=True, to='products.Category', verbose_name='category'),
        ),
    ]
