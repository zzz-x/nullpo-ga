# 文件名:db.py
# 功能：数据库操作
# 功能函数包括：初始化数据库，插入数据，查询数据，更新数据，删除数据，关闭数据库,按照评分排序
from datetime import datetime
import os
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import game_info, game_score, game_type, user_info, comment


# 对game_info,game_type,user_info,comment实现了add,delete,query,update接口
# 生成测试数据库:cmd下 flask initdb --drop,flask forge

# 插入一个game_info
# parm:type_id,game_title,game_description
def add_game(type_id, game_title, game_description, game_company, release_date):
    gt = game_type.query.get(type_id)
    g = game_info(game_title=game_title, game_intro=game_description)
    g.game_type_name = gt.type_name
    gt.games.append(g)

    g.game_release_time = datetime.strptime(release_date, '%Y-%m-%d')
    print(release_date)
    g.game_develop_company = game_company
    if os.path.exists(".\\apps\\static\\gameMaterialStock\\" + str(g.game_id)) == False:
        print("makdir")
        os.mkdir(".\\apps\\static\\gameMaterialStock\\" + str(g.game_id))
    else:
        print("no")
    db.session.commit()
    return g.game_id


def getAllGames():
    return game_info.query.all()


def getalluser():
    return user_info.query.all()


# 查找一个game_info
# parm:title
# ret:game_info-list
def query_game(title):
    _g = game_info.query.filter_by(game_title=title).first()
    if (_g is None):
        return None
    return _g.game_id


# def query_game_by_limit_and_

# 删除一个game_info
# parm:game_id
def delete_game(game_id):
    g = game_info.query.get(game_id)
    db.session.delete(g)
    db.session.commit()


# 根据gameid查找game_info
# parm:game_id
# ret:game_info
def find_game_by_id(game_id):
    g = game_info.query.get(game_id)
    if (g is None):
        return 'fail'
    return g


# 插入一个game_type,传入name(string)
def add_type(name=''):
    gt = game_type(type_name=name)
    db.session.add(gt)
    db.session.commit()
    return gt.type_id


# 查找一个game_type
# parm:name
# ret:game_type-list
def query_type(name):
    gt = game_type.query.filter_by(type_name=name).first()
    if (gt is None):
        return None
    return gt.type_id


# 删除一个game_type
# parm:type_id
def delete_type(type_id):
    gt = game_type.query.get(type_id)
    db.session.delete(gt)
    db.session.commit()


# 插入一个user_info
# parm:name,intro
def add_user(name='', intro=''):
    u = user_info(user_name=name, user_self_intro=intro)
    db.session.add(u)
    db.session.commit()


# 查找一个user_info
# parm:name
# ret:user_info-list
def query_user(name=''):
    u = user_info.query.filter_by(user_name=name).first()
    if (u is None):
        return None
    return u.id


def quer_user_by_id(id):
    u = user_info.query.get(id)
    if (u is None):
        return None
    return u


# 插入一个comment
# parm:game_id,id,contents
def add_comment(game_id, id, contents=''):
    c = comment(comment_contents=contents)
    g = game_info.query.get(game_id)
    u = user_info.query.get(id)
    g.comments.append(c)
    u.comments.append(c)
    print(c.comment_contents)
    db.session.commit()


# 根据用户id查找所有comment
# parm:user_id
# ret:comment(none:-1)
def query_comment_by_user_id(user_id):
    c = comment.query.filter_by(comment_user_id=user_id)
    if (c is None):
        return None
    return c


# 根据游戏id查找所有comment
# parm:game_id,id
# ret:comment(none:-1)
def query_comment_by_game_id(game_id):
    c = comment.query.filter_by(comment_game_id=game_id)
    if (c is None):
        return None
    return c


# 删除一个comment
# parm:comment_id
def delete_user(comment_id):
    u = user_info.query.get(comment_id)
    db.session.delete(u)
    db.session.commit()


# 再对查询到的数据更改后(add和delete操作不包括在内)，运行此函数保存更改
def update_all():
    db.session.commit()


# ***************************************************************************************************
# *******************************新        需          求*********************************************
# ***************************************************************************************************
def update_item_value(id, table_name, table_word, new_value):
    if (table_name == 'game_info'):
        g = game_info.query.get(id)
        if (g is None):
            return 'fail'
        if (table_word == 'game_title'):
            g.game_title = new_value
        if (table_word == 'game_intro'):
            g.game_intro = new_value
        if (table_word == 'game_collect_num'):
            g.game_collect_num = new_value
        if (table_word == 'game_comments_num'):
            g.game_comments_num = new_value

    if (table_name == 'user_info'):
        u = user_info.query.get(id)
        if (u is None):
            return 'fail'
        if (table_word == 'user_name'):
            u.user_name = new_value
        if (table_word == 'user_email'):
            u.user_email = new_value
        if (table_word == 'user_password'):
            u.user_password = new_value
        if (table_word == 'user_self_intro'):
            u.user_self_intro = new_value

    if (table_name == 'game_type'):
        gt = game_type.query.get(id)
        if (gt is None):
            return 'fail'
        if (table_word == 'type_name'):
            gt.type_name = new_value

    if (table_name == 'comment'):
        c = comment.query.get(id)
        if (c is None):
            return 'fail'
        if (table_word == 'comment_contents'):
            c.comment_contents = new_value

    db.session.commit()
    return 'success or no match'


def get_item_value(id, table_name, table_word):
    if (table_name == 'game_info'):
        g = game_info.query.get(id)
        if (g is None):
            return 'fail'
        if (table_word == 'game_title'):
            return g.game_title
        if (table_word == 'game_average_score'):
            return g.game_average_score
        if (table_word == 'game_intro'):
            return g.game_intro
        if (table_word == 'game_collect_num'):
            return g.game_collect_num
        if (table_word == 'game_comments_num'):
            return g.game_comments_num
        if (table_word == 'game_update_time'):
            return g.game_update_time

    if table_name == 'user_info':
        u = user_info.query.get(id)
        if (u is None):
            return 'fail'
        if (table_word == 'comments'):
            return u.comments
        if (table_word == 'user_name'):
            return u.user_name
        if (table_word == 'user_email'):
            return u.user_email
        if (table_word == 'user_password'):
            return u.user_password
        if (table_word == 'user_regis_time'):
            return u.user_regis_time
        if (table_word == 'user_self_intro'):
            return u.user_self_intro

    if (table_name == 'game_type'):
        gt = game_type.query.get(id)
        if (gt is None):
            return 'fail'
        if (table_word == 'type_name'):
            return gt.type_name

    if (table_name == 'comment'):
        c = comment.query.get(id)
        if (c is None):
            return 'fail'
        if (table_word == 'comment_user_name'):
            return c.related_user.user_name
        if (table_word == 'comment_title'):
            return c.comment_title
        if (table_word == 'comment_contents'):
            return c.comment_contents

    return 'no match'


def find_user(id):
    u = user_info.query.get(id)
    if (u is None):
        return 'fail'
    return u


# 删除一个user_info
# parm:id
def delete_user(id):
    u = user_info.query.get(id)
    if (u is None):
        return 'fail'
    db.session.delete(u)
    db.session.commit()
    return 'success'


def check_username_password(name, passw):
    u = user_info.query.filter_by(user_name=name).first()
    if (u is None):
        return "cantfind"
    if (check_password_hash(u.user_password, passw) == False):
        return "passwordincorrect"
    print('yes')
    return u.id


def change_username(id, new_name):
    u = user_info.query.get(id)
    if (u is None):
        return "user no found!"
    un = user_info.query.filter_by(user_name=new_name).first()
    if (un is None):
        u.user_name = new_name
        return 'success'
    else:
        return 'fail'


def add_new_user(name, passw):
    i = user_info.query.filter_by(user_name=name).first()
    if i is None:
        u = user_info(user_name=name, user_password=passw)
        db.session.add(u)
        db.session.commit()
        if not os.path.exists(".\\apps\\static\\userMaterialStock\\" + str(u.id)):
            print("makdir")
            os.mkdir(".\\apps\\static\\userMaterialStock\\" + str(u.id))
        else:
            print("no")
        return u.id
    return 'name has existed'


# ***************************************************************************************************
###########################################################################################
###########################################################################################
###########################################################################################
def collect_game(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    user.collects.append(game)
    db.session.commit()


def incollect_game(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    user.collects.remove(game)
    db.session.commit()


def is_collect(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    num = user.collects.count(game)
    if (num >= 1):
        return True
    else:
        return False


def collect_list(user_id):
    clist = []
    user = user_info.query.get(user_id)
    for game in user.collects:
        clist.append(game)
    return clist


def exper_game(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    user.expers.append(game)
    db.session.commit()


def inexper_game(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    user.expers.remove(game)
    db.session.commit()


def is_exper(user_id, game_id):
    game = game_info.query.get(game_id)
    user = user_info.query.get(user_id)
    num = user.expers.count(game)
    if num >= 1:
        return True
    else:
        return False


def exper_list(user_id):
    elist = []
    user = user_info.query.get(user_id)
    for game in user.expers:
        elist.append(game)
    return elist


def score_list(game_id):
    slist = [0, 0, 0, 0, 0]
    game = game_info.query.get(game_id)
    for score in game.game_scores:
        slist[score.score_value - 1] += 1
    return slist


def add_score(game_id, value):
    score = game_score(score_value=value)
    game = game_info.query.get(game_id)
    game.game_scores.append(score)
    num = 0
    total = 0
    for s in game.game_scores:
        num += 1
        total += int(s.score_value)
    game.game_average_score = float(total) / num
    db.session.commit()


def game_cmp(game):
    if (game.game_average_score is None):
        return 0
    return 5 - game.game_average_score


def all_list():
    games = game_info.query.all()
    games.sort(key=game_cmp)
    return games


def get_games_num():
    return game_info.query.count()


def get_start_and_end_index(total_num, limit, offset):
    start_index = offset * limit
    end_index = start_index + limit
    if start_index > total_num:
        return 0, 0
    if end_index > total_num:
        end_index = total_num
    return start_index, end_index


def get_games(limit, offset):
    # get all games
    games = game_info.query.all()
    games.sort(key=game_cmp)
    start_index, end_index = get_start_and_end_index(len(games), limit, offset)
    return games[start_index:end_index]


def get_games_by_type(typeName, limit, offset):
    # 按照种类筛选，并且按照评分排序
    gt = game_type.query.filter_by(type_name=typeName).first()
    games = gt.games
    games.sort(key=game_cmp)

    start_index, end_index = get_start_and_end_index(len(games), limit, offset)
    return games[start_index:end_index]


def get_games_by_year(begin_year, end_year, limit, offset):
    # 按照年份筛选，并且按照评分排序
    games = game_info.query.all()
    games.sort(key=game_cmp)
    ret = []
    # 删除不在时间范围内的游戏
    for game in games:
        game_release_year = game.game_release_time.year
        if begin_year <= game_release_year <= end_year:
            ret.append(game)

    start_index, end_index = get_start_and_end_index(len(ret), limit, offset)
    return ret[start_index:end_index]


def get_games_by_type_and_year(typeName, begin, end, limit, offset):
    # 按照种类和年份筛选，并且按照评分排序
    gt = game_type.query.filter_by(type_name=typeName).first()
    games = gt.games
    games = games.filter(game_info.game_release_date >= begin, game_info.game_release_date <= end)
    games.sort(key=game_cmp)
    return games


def initdb():
    db.drop_all()
    db.create_all()
    print('***** Datebase created ****')
