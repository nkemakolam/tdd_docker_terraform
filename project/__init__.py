import os
import sys  # new
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # new


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new
print(app.config, file=sys.stderr)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincremet=True)
    username = db.Column(db.string(128),nullable=False)
    email=db.Column(db.string(128),nullable=False)
    active = db.Column(db.Boolean(),default=True,nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
       




class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!',
            'terrafom':'awaiting'
        }


api.add_resource(Ping, '/ping')