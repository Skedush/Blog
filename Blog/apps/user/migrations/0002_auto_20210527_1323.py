# Generated by Django 3.2 on 2021-05-27 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='git',
        ),
        migrations.RemoveField(
            model_name='user',
            name='home',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='用户手机号')),
                ('home', models.CharField(blank=True, max_length=255, null=True, verbose_name='主页')),
                ('git', models.CharField(blank=True, max_length=255, null=True, verbose_name='git地址')),
                ('motton', models.CharField(blank=True, max_length=255, null=True, verbose_name='签名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userInfo', to=settings.AUTH_USER_MODEL, verbose_name='用户Id外键')),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
                'db_table': 'userinfo',
                'ordering': ['-id'],
            },
        ),
    ]
