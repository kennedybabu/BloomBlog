from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment...', validators=[InputRequired()])
    submit = SubmitField('comment')