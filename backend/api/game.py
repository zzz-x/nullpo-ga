from flask import current_app, jsonify, session
from flask_restful import Resource, reqparse
import sys

sys.path.append("..")
from backend.database.DBControl import *
from flask_login import login_required


class GetGame(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('game_id', type=int, required=True)
        args = parser.parse_args()
        game_id = args['game_id']
        game = find_game_by_id(game_id)
        if game is None:
            return {'message': 'Game not found'}, 404
        return jsonify(game)


class UploadGame(Resource):
    def post(selfself):
        return jsonify({"status": "success"})


class Rate(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('game_id', type=int, required=True)
        parser.add_argument('score', type=int, required=True)
        args = parser.parse_args()
        game_id = args['game_id']
        score = args['score']
        if game_id and score:
            add_score(game_id, score)
            game = find_game_by_id(game_id)
            return jsonify({'status': 'success', 'game_average_score': game.game_average_score})


class Comment(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('game_id', type=int, required=True)
        parser.add_argument('comment', type=str, required=True)
        args = parser.parse_args()
        game_id = args['game_id']
        comment_content = args['comment']
        if game_id and comment_content:
            add_comment(game_id, comment_content)
            game = find_game_by_id(game_id)
            return jsonify({'status': 'success', 'game_average_score': game.game_average_score})


class GetAllGames(Resource):
    def get(self):
        games = getAllGames()
        return jsonify(games)