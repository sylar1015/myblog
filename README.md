# myblog
This is a personal website powered by(sylar1015@163.com):
Flask
Flask-Script
Flask-Bootstrap
Flask-WTF
Flask-SQLAlchemy
Flask-Migrate
Flask-PageDown
Flask-Moment
Flask-Login
Flask-Cache
Flask-Admin

Source code of http://www.sylar.site

部署说明：
1、测试环境为centos7 + python3.4 + virtualenv
2、pip -r requirements.txt
3、安装MySQL并创建数据库myblog
4、修改config.py中SQLALCHEMY_DATABASE_URI
5、创建数据库表
    1)、./manage.py db init
    2)、./manage.py db migrate
    3)、./manage.py db upgrade
6、运行
    1)、./manage.py runserver -p 80 -h 0.0.0.0
    2)、gunicorn、nginx...

Release 1.1:
1. 展示/发布文章
2. Bootstrap页面展示
3. 管理员权限
4. 数据库为MySQL
5. 支持数据库迁移/更新
6. 支持缓存

