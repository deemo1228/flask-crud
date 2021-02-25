# # 設置密鑰
# SECRET_KEY = 'many random bytes'


import os
import datetime

# basedir = os.path.abspath(os.path.dirname(__file__))
#  取得目前文件資料夾路徑
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')  # app資料夾


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig:  # 基本配置
    SECRET_KEY = 'THIS IS MAX'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    # 設置資料庫地址以及相關配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:redd00r@192.168.112.141:3306/crud_test'

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}