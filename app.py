from config import Configuration
from flask_login import LoginManager
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Configuration)
db = MongoEngine(app)
login_manager = LoginManager(app)
api = Api(app)

from models import *