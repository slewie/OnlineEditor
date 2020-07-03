from flask import Blueprint, redirect, render_template
from .authorize_forms import *
import mongoengine
authorize = Blueprint('authorize', __name__, template_folder='templates', static_folder='static')
from main import User, db
from flask_login import current_user, LoginManager, login_user, logout_user, login_required


@authorize.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.first(_nickname=form.email_or_nickname.data)
        if not user:
            user = User.objects.first(_email=form.email_or_nickname.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('authorize/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('authorize/login.html', title='Авторизация', form=form)


@authorize.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('authorize/register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        try:
            if User.objects.get(email=form.email.data):
                return render_template('authorize/register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
        finally:
            print(User.set_password(form.password.data))
            User(
                email=form.email.data,
                nickname=form.nickname.data,
                hashed_password=User.set_password(form.password.data)
            ).save()
            return redirect('/')
    return render_template('authorize/register.html', title='Регистрация', form=form)
