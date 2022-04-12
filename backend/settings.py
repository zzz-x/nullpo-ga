import os
import sys


class BaseConf(object):
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = '123456'
    STATIC_FOLDER = os.path.abspath("../static")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__).replace('\\', '/'),
                                                          'database/data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
