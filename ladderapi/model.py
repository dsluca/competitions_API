from ladderapi import APP
from ladderapi import DB
from flask.ext.sqlalchemy import SQLAlchemy

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


class Challenge(DB.Model):
    """DB Object represneting a challenge"""
    challengeId = DB.Column(DB.Integer, primary_key=True)
    player1 = DB.Column(DB.Integer, DB.ForeignKey('player.playerId'))

    def __init__(self, player1):
        self.player1 = player1

    def __repr__(self):
        return '<player1 ' + self.player1 + '> <player2 ' + self.player2 + '>'

