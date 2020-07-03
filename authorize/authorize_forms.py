from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from wtforms import StringField, SubmitField, BooleanField, PasswordField


class LoginForm(FlaskForm):
    email_or_nickname = StringField('Почта или никнейм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    nickname = StringField('Никнейм', validators=[DataRequired()])
    submit = SubmitField('Регистрация')
