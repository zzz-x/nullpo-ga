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

from flask import jsonify, request
from flask_restful import Resource
from flask_login import (login_user, logout_user, current_user)
from werkzeug.security import generate_password_hash
import sys

sys.path.append("..")
from backend.database.DBControl import *

from flask_login import login_required


class SignIn(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if username is None or password is None:
            return {"status": "fail", "message": "Missing username or password"}, 400
        user = check_username_password(username, password)

        if user == 'cantfind':
            return {"status": "fail", "message": "Wrong username or password"}, 400
        elif user == 'passwordincorrect':
            return {"fail": "Wrong username or password"}, 400
        else:
            login_user(find_user(user))
            return {"status": "success", "message": "Login successful"}, 200


class LogOut(Resource):
    @login_required
    def post(self):
        logout_user()
        return {"status": "success", "message": "Logout successful"}, 200


class Register(Resource):
    def post(self):
        # if user is login then return error
        if current_user.is_authenticated:
            return {"status": "fail", "message": "User is already logged in"}, 400
        username = request.form.get('username')
        password = request.form.get('password')
        user = check_username_password(username, password)
        password = generate_password_hash(password)
        if user == 'cantfind':
            add_new_user(username, password)
            return {"status": "success", "message": "Registration successful"}, 200
        else:
            return {"status": "fail", "message": "Username already exists"}, 400
