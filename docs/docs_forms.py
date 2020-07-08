from wtforms import TextAreaField, SubmitField
from flask_wtf import FlaskForm


class DocForm(FlaskForm):
    text_area = TextAreaField('')
    save = SubmitField('Сохранить')
