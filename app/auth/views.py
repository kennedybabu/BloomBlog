from flask import render_template, redirect, url_for, flash
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms import validators
from . import auth
from .. import db
from ..email import mail_message
from ..models import User
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message('Welcome to the BlogBlossom family', "email/welcome_user", user.email, user=user)

        return redirect(url_for('auth.login'))
        title = 'New Account'

    return render_template('auth/register.html', form = form)
         
    

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or password')

    title = 'BlogBlossom login'
    return render_template('auth/login.html', login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


