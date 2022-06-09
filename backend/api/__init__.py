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

from flask import Blueprint
from flask_restful import Api

from .account import GetAccount
from .index import Index
from .auth import SignIn, LogOut, Register
from .game import GetGame, Rate, AddComment, UploadGame, GetAllGames, GetCommentByGameID, GetGames, GetCommentByUserID

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(Index, '/')
# 请求格式：
# /api/signin
# body: [form-data]
# username: str
# password: str
api.add_resource(SignIn, '/api/signin')
# 请求格式：
# /api/signout
api.add_resource(LogOut, '/api/signout')
# 请求格式：
# /api/register
# body: [form-data]
# username: str
# password: str
api.add_resource(Register, '/api/register')
# 请求格式：
# /api/get-account
api.add_resource(GetAccount, '/api/get-account')
# 请求格式：
# /api/get-game?game_id=1
api.add_resource(GetGame, '/api/get-game')
# 请求格式：
# /api/get-games?limit=10&offset=1&start_year=2019&end_year=2020&type_name=PS4
# limt: int, 每页显示的数量
# offset: int, 页码
# limit,offset必选，start_year,end_year,type_name可选
#例如每页十条游戏，则要获取第二页，参数为：limit=10&offset=1
api.add_resource(GetGames, '/api/get-games')
# 请求格式：
# /api/get-all-games
api.add_resource(GetAllGames, '/api/get-all-games')
# 请求格式：
# /api/game/rate?game_id=1&rate=5
api.add_resource(Rate, '/api/game/rate')
# 请求格式：
# /api/game/add-comment
# body: [form-data]
# game_id: int
# comment: str
api.add_resource(AddComment, '/api/game/add-comment')
# 请求格式：
# /api/game/get-comments-by-game_id?game_id=1
api.add_resource(GetCommentByGameID, '/api/game/get-comments-by-game_id')
# 请求格式：
# /api/game/get-comments-by-user_id?user_id=1
api.add_resource(GetCommentByUserID, '/api/game/get-comments-by-user_id')
