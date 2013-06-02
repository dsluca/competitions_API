""" The Tennis Ladder API"""
import os
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
DB = SQLAlchemy(APP)


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
    userx = all_users.pop()
    print all_users
    print userx
    return jsonify(X=userx.email)


@APP.route('/db/create/player/<string:name>/<string:email>', methods=['POST', 'PUT'])
def create_player(name, email):
    """create a new player"""
    print "creating " + email
    player = Player(name, email)
    DB.session.add(player)
    DB.session.commit()
    status = {"status": "OK"}
    return jsonify(result=status)


def get_players():
    """get all players and their ranks in the ladder."""
    dylan = PlayerRank(1, "dylan", 1, 0)
    danny = PlayerRank(2, "danny", 1, 0)
    gerik = PlayerRank(3, "gerik", 1, 0)
    simon = PlayerRank(4, "simon", 1, 0)
    return [dylan.__dict__, danny.__dict__, gerik.__dict__, simon.__dict__]


class PlayerRank:
    """Represents a player and its points"""
    def __init__(self, player_id, username, rank, points):
        self.player_id = player_id
        self.username = username
        self.rank = rank
        self.points = points

    def method1(self):
        """bla"""
        print "methond to keep pylint happy for now " + self.username

    def method2(self):
        """bla"""
        print "methond to keep pylint happy for now "  + self.rank


class Player(DB.Model):
    """DB Object repesenting a player """
    playerId = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    email = DB.Column(DB.String(120), unique=True)
    challenges = DB.relationship('Challenge', backref='player', lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

    def method1(self):
        """bla"""
        print "methond to keep pylint happy for now " + self.name

    def method2(self):
        """bla"""
        print "methond to keep pylint happy for now "  + self.email


class Challenge(DB.Model):
    """DB Object represneting a challenge"""
    challengeId = DB.Column(DB.Integer, primary_key=True)
    player1 = DB.Column(DB.Integer, DB.ForeignKey('player.playerId'))
    player2 = DB.Column(DB.Integer, DB.ForeignKey('player.playerId'))

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return '<player1 ' + self.player1 + '> <player2 ' + self.player2 + '>'

    def method1(self):
        """bla"""
        print "methond to keep pylint happy for now " + self.player2

    def method2(self):
        """bla"""
        print "methond to keep pylint happy for now " + self.player1