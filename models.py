from app import db, login_manager
from flask_login import UserMixin, current_user
import bcrypt


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

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()


class Docs(db.Document):
    author = db.ReferenceField(User)
    text = db.StringField()

    @staticmethod
    def get_doc_id():
        return Docs(text='', author=User.get_user()).save().id