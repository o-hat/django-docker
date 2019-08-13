# django-docker
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
## Docker Images Reference

| Name   | Image                              |
| ------ | ---------------------------------- |
| Nginx  | <https://hub.docker.com/_/nginx/>  |
| MySQL  | <https://hub.docker.com/_/mysql/>  |
| Redis  | <https://hub.docker.com/_/redis/>  |
| Python | <https://hub.docker.com/_/python/> |


## 存在的问题

1. session的问题 在代码中标记了TODO

2. docker 开发环境和生产环境的自动切换

3. docker的静态文件托管问题 nginx和web不在一个同一个容器 所以生成后的static文件 nginx不能托管 目前是直接本地先生成，然后直接把生成的整个目录让nginx托管。但是这样就没有意义了，本地还是要安装环境。
这个问题解决了！ 因为python manage.py collectstatic 生成的文件夹 是宿主机上的文件夹 同时由nginx托管。

4. UI的整理

5. 

## TODOLIST（8.12）

- 博客从gitbook改用开源的vuepress 3天
- 把以前的资料整理一下 对做过的项目进行总结 3天
- 想好自己会什么 1天
- 想好要什么 1天
- 针对性复习 2天
- 针对性完善简历 0.5天
- 投简历 面试
