from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)  # 自增长
    name = models.CharField(max_length=30, verbose_name='分类名称')  # 长度做多30的字符串
    describe = models.CharField(
        max_length=254, verbose_name='分类描述', null=True, blank=True)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建时间')  # auto_now_add创建时自动将创建的时间插入
    update_time = models.DateTimeField(
        auto_now=True, verbose_name='修改时间')  # auto_now更新时自动将时间插入
    is_delete = models.BooleanField(
        default=False, verbose_name='是否删除')  # default默认为False
    sort = models.IntegerField(default=999, verbose_name='分类排序')  # 默认为999
    # 自关联多对多关系，指定多对多关系表名称为category_ship,取消对称关联symmetrical
    parent = models.ManyToManyField(
        'self', db_table='category_ship', symmetrical=False, blank=True, related_name='children')

    def __str__(self):  # 输出对象实例或str()对象实例调用的方法
        return self.name

    class Meta:
        db_table = 'category'  # 指定表名为category
        ordering = ['sort', 'id']  # 排序
        verbose_name = '分类'  # 可读单数名称
        verbose_name_plural = verbose_name  # 可读复数名称


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=100, verbose_name='标题', blank=False, null=False)
    sub_title = models.CharField(
        max_length=200, verbose_name='副标题', blank=True, null=True)
    content = models.TextField(verbose_name='文档内容', blank=False, null=False)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    sort = models.IntegerField(default=999, verbose_name='文章排序')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    category = models.ManyToManyField(
        Category,  related_name='articles', related_query_name='article',  db_table='article_category_ship')

    def __str__(self):  # 输出对象实例或str()对象实例调用的方法
        return self.title

    class Meta:
        db_table = 'article'
        ordering = ['id']
        verbose_name = '文章'
        verbose_name_plural = verbose_name
