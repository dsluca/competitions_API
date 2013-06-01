import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def home():
	print "does this log?"
	return jsonify(status="OK")

@app.route('/ladder/get')
def getLadder():
	l = Ladder()
	return jsonify(players=l.getPlayers())


class Ladder:
	"""Ladder """

	def getPlayers(self):
		dylan = PlayerRank(1,"dylan",1,0)
		danny = PlayerRank(2,"danny",1,0)
		gerik = PlayerRank(3,"gerik",1,0)
		simon = PlayerRank(4,"simon",1,0)
		return [dylan.__dict__, danny.__dict__, gerik.__dict__, simon.__dict__]

class PlayerRank:
	"""Represents a player and its points """
	def __init__(self,playerId,username,rank, points):
		self.playerId = playerId
		self.username = username
		self.rank = rank
		self.points = points

@app.route('/db/test')
def dbTest():
	print "OK"
	print "querying"
	all_users = Player.query.all()
	userx = all_users.pop()
	print all_users
	print userx
	return jsonify(X=userx.email)


@app.route('/db/create/player/<string:name>/<string:email>')
def create_db(name, email):
	print "creating " + email
	player = Player(name, email)
	db.session.add(player)
	db.session.commit()
	status = {"status": "OK"}
	return jsonify(result=status)

'''
Model
'''
class Player(db.Model):
	playerId = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	email = db.Column(db.String(120), unique=True)
	challenges = db.relationship('Challenge', backref='player', lazy='dynamic')

	def __init__(self, name, email):
		self.name = name
		self.email = email

	def __repr__(self):
		return '<Name %r>' % self.name


class Challenge(db.Model):
	challengeId = db.Column(db.Integer, primary_key=True)
	player1 = db.Column(db.Integer, db.ForeignKey('player.playerId'))
	player2 = db.Column(db.Integer, db.ForeignKey('player.playerId'))

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
