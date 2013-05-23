import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify(status="OK")

@app.route('/ladder/get')
def getLadder():
	l = Ladder()
	dylan = PlayerRank(1,"dylan",1,0)
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

	
