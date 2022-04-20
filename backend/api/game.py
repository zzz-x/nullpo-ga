from flask import jsonify
from flask_restful import Resource, reqparse, request
import sys

sys.path.append("..")
from backend.database.DBControl import *
from flask_login import login_required


# GetGame
# args: game_id (get args from the url↓)
# url: localhost:5000/api/get-game?game_id=<game_id>
class GetGame(Resource):
    def get(self):
        # lcoalhost:5000/api/game?game_id=1
        # get url
        game_id = request.args.get('game_id')
        game = find_game_by_id(game_id)

        # print(game_id)
        if game is None:
            return {'message': 'Game not found'}, 404
        res = []
        res.append(game.as_dict())

        return jsonify({'status': 'success', 'data': res})


# UpdateGame
class UploadGame(Resource):
    def post(selfself):
        return jsonify({"status": "success"})


# Rate
# args: game_id, score (get agrs from the url↓)
# url: localhost:5000/api/game/rate?<game_id>&<score>
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


# AddComment
# args: game_id, comment (get args from form)
class AddComment(Resource):
    @login_required
    def post(self):
        game_id = request.form['game_id']
        comment_content = request.form['comment']
        if game_id and comment_content:
            add_comment(game_id, comment_content)
            game = find_game_by_id(game_id)
            return jsonify({'status': 'success', 'game_average_score': game.game_average_score})


# GetCommentByGameId
# args: game_id (get args from the url↓)
# url: localhost:5000/api/game/get-comment?game_id=<game_id>
class GetCommentByGameID(Resource):
    def get(self):
        game_id = request.args.get('game_id')
        # data1: comment set data2:the user set who send the comment
        comments = query_comment_by_game_id(game_id)
        if comments is None:
            return {'message': 'Game not found'}, 404
        comment_res = []
        for comment in comments:
            comment_res.append(comment.as_dict())

        user_res = []
        for comment in comment_res:
            user = quer_user_by_id(comment['comment_user_id'])
            user_res.append(user.as_dict())

        return jsonify({"status": "success", "comments": comment_res, "users": user_res})


class GetAllGames(Resource):
    def get(self):
        games = getAllGames()
        # jsonify
        res = []
        for game in games:
            res.append(game.as_dict())
        return jsonify(res)
