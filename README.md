# Blog

基于 django rest framework 博客系统的后台 api

---

## 安装依赖

```
$pip install -r Blog/requirements.txt
```

---

## 项目配置修改

1. 在 setting/commom 中修改数据库信息

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用的引擎，需要安装 PyMySQL 包
        'NAME': 'blog',  # 连接数据库的名称
        'USER': 'root',  # 连接数据库的用户名
        'PASSWORD': 'root',  # 连接数据库的密码
        'HOST': '127.0.0.1',  # 连接数据库的地址
        'PORT': '3306',  # 连接数据库的端口
    }
}
```

2. 创建数据库与 NAME 指定的一样

3. 执行数据库初始化命令

由于数据库迁移文件已经上传，直接执行：

```
$python manage.py migrate
```

---

## 项目启动

```
$python manage.py runserver --setting=Blog.settings.dev
```
