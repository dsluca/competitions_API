from ladderapi import APP, DB, model
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from ladderapi import model
from model import Player


@APP.route('/')
def home():
    """root path."""
    print "does this log?"
    return jsonify(status="OK")


@APP.route('/ladder/get', methods=['GET'])
def get_ladder():
    """Get a ladder."""
    return jsonify(players=get_players())


@APP.route('/db/test')
def db_test():
    """Test the connection to the db is fine."""
    print "OK"
    print "querying"
    all_users = Player.query.all()
    print "..."
    print all_users
    userx = all_users.pop()
    print userx
    return jsonify(X=userx.email)


@APP.route('/create/player/<string:name>/<string:email>', methods=['POST', 'PUT'])
def create_player(name, email):
    """create a new player"""
    try:
        player = Player(name, email)
        DB.session.add(player)
        DB.session.commit()
    except Exception as e:
        print "exception caught", sys.exc_info()[0]
        status = {"status": "ERROR"}
    else:
        status = {"status": "OK"}
    finally:
        return jsonify(result=status)


@APP.route('/update/player/<int:id>', methods=['POST', 'PUT'])
def update_player(id):
    print id
    player = request.json
    return jsonify(status="OK")

@APP.route('/json/test', methods=['POST', 'PUT'])
def json_test():
    req_obj = request.json
    print req_obj['status']
    return jsonify(x="OK")


def get_players():
    """get all players and their ranks in the ladder."""
    dylan = PlayerRank(1, "dylan", 1, 0)
    danny = PlayerRank(2, "danny", 1, 0)
    gerik = PlayerRank(3, "gerik", 1, 0)
    simon = PlayerRank(4, "simon", 1, 0)
    return [dylan.__dict__, danny.__dict__, gerik.__dict__, simon.__dict__]


class PlayerRank:
    """Represents a player and its points. This is only temp.. i will likely remove it"""
    def __init__(self, player_id, username, rank, points):
        self.player_id = player_id
        self.username = username
        self.rank = rank
        self.points = points
