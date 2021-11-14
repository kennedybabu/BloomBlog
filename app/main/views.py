from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..request import get_quotes
from app import db, photos
from ..models import Blog, Comment, User
from .forms import CommentForm, BlogForm, UpdateProfile
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
        return redirect(url_for('main.show_blogs'))

    return render_template('create_blog.html', form = form)

@main.route('/<title>/update_blog', methods=['POST', 'GET'])
@login_required
def update_blog(title):
    blog = Blog.query.filter_by(title = title).first()
    form = BlogForm

    if form.validate_on_submit():
        title = form.title.data
        blog_content = form.blog_content.data
        author_id = current_user.id
        db.session.add(blog)
        db.session.commit()

        flash('blog updated')
        return redirect(url_for('main.show_blogs', author_id = author_id, blog_content = blog_content))

    return render_template('main.update_blog.html', form = form)


@main.route('/blogs')
def show_blogs():
    blogs = Blog.query.order_by(Blog.posted.desc())

    return render_template('show_blogs.html', blogs = blogs)


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


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))


