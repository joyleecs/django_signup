# Generated by Django 3.0.1 on 2019-12-19 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20191219_1037'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Fcuser',
        ),
    ]
