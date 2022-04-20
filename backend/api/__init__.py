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

from .account import Account
from .index import Index
from .auth import SignIn, LogOut, register
from .game import GetGame, Rate, AddComment, UploadGame, GetAllGames, GetCommentByGameID

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(Index, '/')
api.add_resource(SignIn, '/api/signin')
api.add_resource(LogOut, '/api/signout')
api.add_resource(register, '/api/register')
api.add_resource(Account, '/api/get-account')
api.add_resource(GetGame, '/api/get-game')
api.add_resource(GetAllGames, '/api/get-all-games')
api.add_resource(Rate, '/api/game/rate')
api.add_resource(AddComment, '/api/game/add-comment')
api.add_resource(GetCommentByGameID, '/api/game/get-comments')
