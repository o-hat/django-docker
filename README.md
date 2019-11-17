# django-docker

:sleepy: :yum: :mask: :sunglasses: :dizzy_face: :sweat: :hushed: :open_mouth: :rage4: :speak_no_evil: :baby:

A complete example for deploying Django project with Nginx and MySQL on Docker.

## QuickStart
Install Docker Engine from the tutorial <https://docs.docker.com/engine/installation/>.</br>
Install Docker Compose from the tutorial <https://docs.docker.com/compose/install/>.</br>
Get the latest project clone to your computer:
```bash
$ git clone https://github.com/huchenw/django-docker.git
```
Run docker-compose commands to start containers:
```bash
$ docker-compose up -d
CREATE DATABASE IF NOT EXISTS blog default charset utf8 COLLATE utf8_general_ci;
# 测试库
CREATE DATABASE IF NOT EXISTS test_blog default charset utf8 COLLATE utf8_general_ci;
```



Now you can access the application at <http://localhost> or <http://192.168.99.100>(Docker Toolbox).</br>
## Static Files
To collect static files for nginx to access, just run:
```bash
$ docker-compose exec web bash
$ python manage.py collectstatic
```
## Django Admin
If you want to access django admin site, please apply the django default migrations to database:
```bash
$ docker-compose exec web bash
$ python manage.py migrate

```
Then you need to create a superuser account:
```bash
$ python manage.py createsuperuser
$ ...
```
## Celery Results
Redis is used as broker for Celery <http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html>.</br>
The official tutorial <http://docs.celeryproject.org/en/latest/django/> tells us how to use Celery with Django.</br>
You can check the Celery results from logs:
```bash
$ docker-compose logs celery
```

## 部署上去的时候碰到的问题
mysql无法连接： chown -R root:root ./


## 存在的问题

1. session的问题 在代码中标记了TODO
2. docker 开发环境和生产环境的自动切换
4. UI的整理
5. 

## 被恶心到了 

很久之前的代码，但是用数据库迁移的命令会报错，而且找不到是哪个表，太不好找bug了！！！！！！！！！

把容器的数据导出来了 /data/blog.sql

## 下一步  基于docker搞敏捷开发 慢慢把博客做好 然后把数据再整理一遍



## python manage.py makemigrations 报错的问题

因为没有对数据库迁移的文件进行版本管理，所以clone下的代码在执行python manage.py makemigrations会报没有改变
然后执行migrate的时候就会报错，导致找了这么久的问题。！！！！！FUCK!!!!!
这个命令执行，没有出现migrations文件夹的时候就纳闷了！！ 但是看执行结果并没有报错，就在找别的问题了！！！FUCK。

数据迁移 不看源代码的划 太不好用了 吐槽一下

还是用flask吧


## bug解决了
1. mysql容器添加了端口映射 连接数据库更加方便
2. mysql备份上服务器的数据
3. 数据库迁移的真的不好用
4. mysql添加了配置文件
5. 去除了https
6. 数据库迁移文件加入版本管理、并且python manage.py makemigrations 后面要加app的lable!!!!(被这个恶心了几个小时)


## TODOLIST

1. 敏捷开发 持续集成 CI CD
2. 表情的bug
3. 邮件提醒
4. seo
5. 整理数据