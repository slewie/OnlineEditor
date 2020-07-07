from wtforms import TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class DocForm(FlaskForm):
    text_area = TextAreaField('')
    save = SubmitField('Сохранить')
