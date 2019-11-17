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
