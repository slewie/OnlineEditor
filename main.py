from flask import Flask, jsonify, request
from config import Configuration
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Configuration)

mongo = MongoEngine(app)
mongo.db.user.insert({'name': 'name'})
if __name__ == '__main__':
    app.run()
