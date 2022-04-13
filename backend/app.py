# Copyright 2022 The Casdoor Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import click
from flask import Flask
from flask_cors import CORS
from api import api_blueprint
from flask_login import (LoginManager, login_user, logout_user, login_required)
from settings import BaseConf
from database.DBControl import *

app = Flask(__name__)
app.config.from_object(BaseConf)
app.register_blueprint(api_blueprint)
CORS(app, supports_credentials=True)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
@login_manager.user_loader  # 初始化管理器
def load_user(user_id):  # 根据user_id返回user对象
    return find_user(user_id)


@click.command()
@click.option('--init_db', is_flag=True, help='init database')
def init_db0(init_db):
    if init_db:
        with app.app_context():
            initdb()


if __name__ == '__main__':
    # init_db0()
    app.run(debug=True)
