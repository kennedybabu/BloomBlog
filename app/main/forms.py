from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms import validators
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment...', validators=[InputRequired()])
    submit = SubmitField('comment')

class BlogForm(FlaskForm):
    title = StringField('your blog title...', validators=[InputRequired()])
    blog_content = TextAreaField("what's your blog all about...", validators=[InputRequired()])
    category = RadioField('pick a category where blog falls into', validators=[InputRequired()], choices=[('lifestyle'), ('food'), ('travel'), ('fashion')])
    submit = SubmitField('create blog')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell people about yourself...')
    submit = SubmitField('submit')