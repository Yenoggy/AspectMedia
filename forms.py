from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Добавить статью')