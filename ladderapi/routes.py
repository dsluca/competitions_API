from ladderapi import APP, DB, model
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from ladderapi import model
from model import Player, Competition
import json


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
    all_users = Player.query.all()
    userx = all_users.pop()
    return jsonify(X=userx.email)


@APP.route('/create/player/', defaults={'name': None, 'email': None},
           methods=['POST', 'PUT'])
@APP.route('/create/player/<string:name>/<string:email>',
           methods=['POST', 'PUT'])
def create_player(name, email):
    """create a new player"""
    try:
        if (request.form.get('name', None) is not None):
            name = request.form['name']
            email = request.form['email']
        player = Player(name, email)
        DB.session.add(player)
        DB.session.commit()
        res = {"status": "OK",
               "playerId": player.playerId,
               "name": player.name,
               "email": player.email}
    except Exception as e:
        print "exception caught", sys.exc_info()[0]
        res = {"status": "ERROR"}
    finally:
        return jsonify(result=res)


@APP.route('/update/player/<int:id>', methods=['POST', 'PUT'])
def update_player(id):
    print id
    player = request.json
    return jsonify(status="OK")


@APP.route('/get/competition_players/<int:competition_id>', methods=['GET'])
def get_competition_players(competition_id):
    """Get the players in a competition / ladder """
    competition = Competition.query.filter_by(
        competitionId=competition_id).first()
    print competition.players
    return jsonify(players=None)


@APP.route('/create/competition/<string:name>', methods=['PUT', 'POST'])
def create_competition(name):
    """Create a competition"""
    competition = Competition(name)
    DB.session.add(competition)
    DB.session.commit()
    return jsonify(competition=competition.competitionId)


@APP.route('/register/player/<int:player_id>/in/competition/<int:competition_id>',
           methods=['PUT', 'POST'])
def register_player_in_league(player_id, competition_id):
    """Register / Add a player to a league"""
    player = Player.query.filter_by(playerId=player_id).first()
    if (player.playerId == player_id):
        competition = Competition.query.filter_by(
            competitionId=competition_id).first()
        print competition.players
        competition.players.append(player)
        DB.session.commit()
        mapped = map(lambda x: {x.name, x.email}, competition.players)
        print mapped
        return jsonify(result=mapped)
    else:
        return jsonify(status="player not found")


def get_players():
    """get all players and their ranks in the ladder."""
    dylan = PlayerRank(1, "dylan", 1, 0)
    danny = PlayerRank(2, "danny", 1, 0)
    gerik = PlayerRank(3, "gerik", 1, 0)
    simon = PlayerRank(4, "simon", 1, 0)
    return [dylan.__dict__, danny.__dict__, gerik.__dict__, simon.__dict__]


class PlayerRank:
    """Represents a player and its points.
    This is only temp.. i will likely remove it"""
    def __init__(self, player_id, username, rank, points):
        self.player_id = player_id
        self.username = username
        self.rank = rank
        self.points = points
