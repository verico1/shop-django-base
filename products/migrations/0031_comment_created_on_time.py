# Generated by Django 3.1.5 on 2021-03-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_remove_comment_created_on_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_on_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
