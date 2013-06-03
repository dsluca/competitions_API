""" The Tennis Ladder API"""
import os
import sys
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
APP.debug = True
DB = SQLAlchemy(APP)


@APP.errorhandler(405)
@APP.errorhandler(404)
def not_allowed(error):
    return jsonify(http_status=error.code, description=error.name)


import ladderapi.model
import ladderapi.routes
