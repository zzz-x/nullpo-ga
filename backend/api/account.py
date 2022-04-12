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

from casdoor import CasdoorSDK
from flask import current_app, jsonify, session
from flask_restful import Resource
from flask_login import current_user

from .utils import authz_required


class Account(Resource):

    @authz_required
    def get(self):
        return jsonify({"status": "success", "data": current_user.to_dict()})


