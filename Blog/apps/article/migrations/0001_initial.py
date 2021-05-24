# Generated by Django 3.2 on 2021-05-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('describe', models.CharField(blank=True, max_length=254, null=True, verbose_name='分类描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('sort', models.IntegerField(default=999, verbose_name='分类排序')),
                ('parent', models.ManyToManyField(blank=True, db_table='category_ship', related_name='children', to='article.Category')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'category',
                'ordering': ['sort', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='副标题')),
                ('content', models.TextField(verbose_name='文档内容')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sort', models.IntegerField(default=999, verbose_name='文章排序')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ManyToManyField(db_table='article_category_ship', related_name='articles', related_query_name='article', to='article.Category')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
                'ordering': ['id'],
            },
        ),
    ]