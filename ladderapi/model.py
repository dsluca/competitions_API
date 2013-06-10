from ladderapi import APP
from ladderapi import DB
from flask.ext.sqlalchemy import SQLAlchemy


player_competitions = DB.Table('player_competitions',
                               DB.Column('competitorId', DB.Integer,
                                         DB.ForeignKey('competitor.competitorId')),
                               DB.Column('competitionId',
                                         DB.Integer,
                                         DB.ForeignKey('competition.competitionId'))
                              )


class Competitor(DB.Model):
    """DB Object repesenting a competitor """
    competitorId = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80))
    email = DB.Column(DB.String(120), unique=True)
    games_home = DB.relationship('Game_Home', backref='competitor_home', lazy='dynamic')
    games_away = DB.relationship('Game_Away', backref='competitor_away', lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


class Competition(DB.Model):
    """DB Object representing a competition"""
    competitionId = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(120), unique=True)
    competitors = DB.relationship('Competitor', secondary=player_competitions,
                              backref=DB.backref('competitors', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name


class Game(DB.Model):
    """DB Object represneting a challenge"""
    gameId = DB.Column(DB.Integer, primary_key=True)
    competitor_home = DB.Column(DB.Integer, DB.ForeignKey('competitor.competitorId'))
    competitor_away = DB.Column(DB.Integer, DB.ForeignKey('competitor.competitorId'))
    competition = DB.Column(DB.Integer, DB.ForeignKey('competition.competitionId'))

    def __init__(self, competition, competitor_home, copetitor_away):
        self.competition = competition
        self.competitor_home = competitor_home
        self.competitor_away = competitor_away

    def __repr__(self):
        return '<Home  ' + self.competitor_home + '> <Away ' + self.competitor_away + '>'
