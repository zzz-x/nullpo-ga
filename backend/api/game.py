from flask import jsonify
from flask_restful import Resource, reqparse, request
from flask_login import current_user, login_required
import sys

sys.path.append("..")
from backend.database.DBControl import *


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
        res = [game.as_dict()]

        return jsonify({'status': 'success', 'data': res})


# GetGames
# args:
#   limit: n, games per page
#   page: n, page number
class GetGames(Resource):
    def get(self):
        # localhost:5000/api/get-games?limit=10&offset=1
        # get url
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        type_name = request.args.get('type_name')
        start_year = request.args.get('start_year')
        end_year = request.args.get('end_year')

        games = []

        # limit or offset is None , return none
        if limit is None or offset is None:
            return {'message': 'limit or offset is None'}, 400

        # 只有开始年份 则查询该年份以后的所有游戏
        if start_year is not None and end_year is None:
            end_year = '9999'
        # 只有结束年份 则查询该年份以前的所有游戏
        if start_year is None and end_year is not None:
            start_year = '1970'

        if start_year is not None:
            start_year = int(start_year)

        if end_year is not None:
            end_year = int(end_year)

        if type_name and start_year and end_year:
            games = get_games_by_type_and_year(type_name, start_year, end_year, limit, offset)
        elif type_name:
            games = get_games_by_type(type_name, limit, offset)
        elif start_year and end_year:
            games = get_games_by_year(start_year, end_year, limit, offset)
        else:
            games = get_games(limit, offset)

        # print(games)
        if games is None:
            return {'message': 'Games not found'}, 404
        res = []
        for game in games:
            res.append(game.as_dict())

        return jsonify({'status': 'success', 'data': res})


# UpdateGame
class UploadGame(Resource):
    def post(selfself):
        return jsonify({"status": "success"})


# Rate
# args: game_id, score (get agrs from the url↓)
# url: localhost:5000/api/game/rate?game_id=<game_id>&score=<score>
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
        print(current_user.id)
        game_id = request.form['game_id']
        comment_content = request.form['comment']
        if game_id and comment_content:
            user_id = current_user.id
            add_comment(game_id, user_id, comment_content)
            game = find_game_by_id(game_id)
            return jsonify({'status': 'success', 'game_average_score': game.game_average_score})


# GetCommentByGameId
# args: game_id (get args from the url↓)
# url: localhost:5000/api/game/get-comments-by-game_id?game_id=<game_id>
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


# GetCommentByUserId
# args: user_id (get args from the url↓)
# url: localhost:5000/api/game/get-comments-by-user_id?user_id=<user_id>
class GetCommentByUserID(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        comments = query_comment_by_user_id(user_id)
        if comments is None:
            return {'message': 'Game not found'}, 404
        comment_res = []
        for comment in comments:
            comment_res.append(comment.as_dict())

        return jsonify({"status": "success", "comments": comment_res})


class GetAllGames(Resource):
    def get(self):
        games = getAllGames()
        # jsonify
        res = []
        for game in games:
            res.append(game.as_dict())
        return jsonify(res)

# SearchGame
# args: keyword (get args from the url↓)
# url: localhost:5000/api/game/search?keyword=<keyword>
class SearchGame(Resource):
    def get(self):
        keyword = request.args.get('keyword')
        if keyword is None:
            return {'message': 'keyword is None'}, 400
        games = search_game(keyword)
        if games is None:
            return {'message': 'Game not found'}, 404
        res = []
        for game in games:
            res.append(game.as_dict())

        return jsonify({'status': 'success', 'data': res})

#  CollectGame
# args: game_id (get args from the url↓)
# url: localhost:5000/api/game/collect?game_id=<game_id>
class CollectGame(Resource):
    @login_required
    def post(self):
        game_id = request.args.get('game_id')
        if game_id:
            user_id = current_user.id
            collect_game(user_id, game_id)
            return jsonify({'status': 'success'})
        else:
            return {'message': 'game_id is None'}, 400

# UncollectGame
# args: game_id (get args from the url↓)
# url: localhost:5000/api/game/uncollect?game_id=<game_id>
class UncollectedGame(Resource):
    @login_required
    def post(self):
        game_id = request.args.get('game_id')
        if game_id:
            user_id = current_user.id
            uncollect_game(user_id, game_id)
            return jsonify({'status': 'success'})
        else:
            return {'message': 'game_id is None'}, 400

# GetCollectedGames
# args: user_id (get args from the url↓)
# url: localhost:5000/api/game/get-collected-games?user_id=<user_id>
class GetCollectedGames(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        if user_id is None:
            user_id = current_user.id
            if user_id is None:
                return {'message': 'user_id is None'}, 400
            else:
                games = collect_list(user_id)
        else:
            games = collect_list(user_id)

        if games is None:
            return {'message': 'Game not found'}, 404
        res = []
        for game in games:
            res.append(game.as_dict())

        return jsonify({'status': 'success', 'data': res})

# IsCollected
# args: game_id (get args from the url↓)
# url: localhost:5000/api/game/is-collected?game_id=<game_id>
class IsCollected(Resource):
    def get(self):
        game_id = request.args.get('game_id')
        if game_id is None:
            return {'message': 'game_id is None'}, 400
        user_id = current_user.id
        if is_collect(user_id, game_id):
            return jsonify({'status': 'success', 'is_collected': True})
        else:
            return jsonify({'status': 'success', 'is_collected': False})

