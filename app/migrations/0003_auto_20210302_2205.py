# Generated by Django 3.1.5 on 2021-03-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_notification'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notification',
            new_name='note',
        ),
    ]