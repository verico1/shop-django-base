# Generated by Django 3.1.5 on 2021-03-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_remove_product_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[(' ', 'موجود'), ('un', 'ناموجود')], max_length=2, null=True, verbose_name='status'),
        ),
    ]