# Generated by Django 3.1.5 on 2021-03-18 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20210317_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_status',
        ),
    ]
