from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    gender_type_choices = (
        ('0', '女'),
        ('1', '男'),
    )
    gender = models.CharField(
        max_length=2, default='1', choices=gender_type_choices, verbose_name='性别')
    date_update = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    phone = models.CharField(max_length=11, null=True,
                             blank=True, verbose_name='用户手机号')
    home = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='主页')
    git = models.CharField(max_length=255, null=True,
                           blank=True, verbose_name='git地址')

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['-id']
