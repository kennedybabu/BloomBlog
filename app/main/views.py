from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..request import get_quotes
from app import db
from ..models import Blog, Comment, User
from .forms import CommentForm, BlogForm
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quotes()
    title = 'Home, BlogBlossom'
    return render_template('index.html', title = title, quote = quote)


@main.route('/blog/<int:id>')
def blog(id):
    '''
    view blog page function that will return the blog item
    '''
    # blog = get_blog
    return render_template('blog.html', blog_id = id)


@main.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    
    form = BlogForm()

    if form.validate_on_submit():
        blog = Blog(title = form.title.data, blog_content = form.blog_content.data, author_id = current_user.id)
        db.session.add(blog)
        db.session.commit()

        flash('blog created')
        return redirect(url_for('blog.show_blogs'))

    return render_template('create_blog.html', form = form)


@main.route('/blog/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    form = CommentForm()

    return render_template('new_comment.html', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('/profile/profile.html',user = user)


