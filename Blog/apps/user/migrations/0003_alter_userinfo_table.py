# Generated by Django 3.2 on 2021-05-27 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210527_1323'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userinfo',
            table='user_info',
        ),
    ]
