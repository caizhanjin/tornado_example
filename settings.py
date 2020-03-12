# encoding: utf-8
import os

from sqlalchemy import create_engine
from tornado.options import define
from libs.db.oracle import DbOracle
from configs import initialize_logging


# 编码设置
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

define("port", default=8001, help="Run server on a specific port", type=int)
define("host", default="localhost", help="Run server on a specific host")

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_BASE_PATH = os.path.join(ROOT_PATH, "logs")

# 日志初始化
initialize_logging(LOG_BASE_PATH)

# environment setting : develop or production
environment = "develop"
if environment == "production":
    print('生产环境！！！')
    DEBUG = False
    DB_ORACLE = {
        'USER': '',
        'PASSWORD': '',
        'NAME': '',
        'HOST': '',
        'PORT': '',
        'charset': ''
    }
else:
    print('开发环境...')
    DEBUG = True
    DB_ORACLE = {
        'USER': '',
        'PASSWORD': '',
        'NAME': '',
        'HOST': '',
        'PORT': '',
        'charset': ''
    }

# the application settings
MEDIA_PATH = os.path.join(ROOT_PATH, 'media')
TEMPLATE_PATH = os.path.join(ROOT_PATH, 'templates')

settings = {
    "debug": DEBUG,
    "static_path": MEDIA_PATH,
    "template_loader": TEMPLATE_PATH,
    "cookie_secret": "xhIBBR2lSp2Pfpx4iiIyX/X6K9j7VUB9oNeA+YdS+ng=",
    # "xsrf_cookies": True,
}

ORACLE_ENGINE = DbOracle(
    DB_ORACLE["USER"],
    DB_ORACLE["PASSWORD"],
    DB_ORACLE["NAME"],
    DB_ORACLE["HOST"],
    DB_ORACLE["PORT"],
)

ORM_URL = 'oracle://{}:{}@{}:{}/?service_name={}'.format(
    DB_ORACLE['USER'],
    DB_ORACLE['PASSWORD'],
    DB_ORACLE['HOST'],
    DB_ORACLE['PORT'],
    DB_ORACLE['NAME']
)
ORM_ENGINE = create_engine(ORM_URL, echo=True)
