# Generated by Django 3.1.5 on 2021-03-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20210314_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_name_fa',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_fa',
            field=models.CharField(default='', max_length=60),
        ),
    ]
