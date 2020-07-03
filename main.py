from flask import Flask, render_template, redirect
from config import Configuration
from flask_mongoengine import MongoEngine
from authorize.authorize import authorize
from docs.docs import docs
from flask_login import current_user, LoginManager, login_user, logout_user, login_required, UserMixin
import bcrypt

app = Flask(__name__)
app.config.from_object(Configuration)
db = MongoEngine(app)

app.register_blueprint(authorize)
app.register_blueprint(docs)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


class User(db.Document, UserMixin):
    nickname = db.StringField(required=True)
    email = db.EmailField(required=True)
    hashed_password = db.StringField(required=True)
    remember_me = db.BooleanField()

    @staticmethod
    def set_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    @staticmethod
    def check_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    @staticmethod
    def get_user():
        return User.objects(id=current_user.id).first()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
