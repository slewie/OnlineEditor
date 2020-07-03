from config import Configuration
from flask_login import LoginManager
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object(Configuration)
db = MongoEngine(app)
login_manager = LoginManager(app)

from models import *