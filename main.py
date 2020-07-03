from flask import Flask, render_template
from config import Configuration
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash
from authorize.authorize import authorize
from flask_login import current_user, LoginManager, login_user, logout_user, login_required

app = Flask(__name__)
app.config.from_object(Configuration)
db = MongoEngine(app)
app.register_blueprint(authorize)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.objects.first(_id=user_id)


class User(db.Document):
    nickname = db.StringField(required=True)
    email = db.EmailField(required=True)
    hashed_password = db.StringField(required=True)
    remember_me = db.BooleanField()

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
