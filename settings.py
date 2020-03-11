# encoding: utf-8
import os
import tornado.web
import tornado.template

from tornado.options import define
from urls import urls_patterns as url_handlers
from libs.db.oracle import DbOracle

# 编码设置
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

define("port", default=8001, help="Run server on a specific port", type=int)
define("host", default="localhost", help="Run server on a specific host")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# environment setting : develop or production
environment = "develop"
if environment == "production":
    print('生产环境！！！')
    DEBUG = False
    DB_ORACLE = {
        'USER': 'tdms',  # 用户名
        'PASSWORD': 'swd_2019_tdms1314',  # 密码
        'NAME': 'orcl',  # 数据库名称
        'HOST': '172.30.201.21',  # HOST
        'PORT': '1521',  # 端口
        'charset': 'utf8'
    }
else:
    print('开发环境...')
    DEBUG = True
    DB_ORACLE = {
        'USER': 'tdms',  # 用户名
        'PASSWORD': 'swd2018tdms',  # 密码
        'NAME': 'orcl',  # 数据库名称
        'HOST': '172.30.201.56',  # HOST
        'PORT': '1521',  # 端口
        'charset': 'utf8'
    }

# the application settings
MEDIA_PAT = os.path.join(BASE_DIR, 'media')
TEMPLATE_PAT = os.path.join(BASE_DIR, 'templates')

settings = {
    "debug": DEBUG,
    "static_path": MEDIA_PAT,
    "cookie_secret": "xhIBBR2lSp2Pfpx4iiIyX/X6K9j7VUB9oNeA+YdS+ng=",
    "xsrf_cookies": True,
}


# 数据库等引入
class Application(tornado.web.Application):
    def __init__(self, handlers, **setting):
        tornado.web.Application.__init__(self, handlers, **setting)
        self.db = DbOracle(
            DB_ORACLE["USER"],
            DB_ORACLE["PASSWORD"],
            DB_ORACLE["NAME"],
            DB_ORACLE["HOST"],
            DB_ORACLE["PORT"],
        )


application = Application(url_handlers, **settings)
