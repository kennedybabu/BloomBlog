from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_quotes
from ..models import Comment
from .forms import CommentForm

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quotes()
    title = 'Home, BlogBlossom'
    print(quote)
    return render_template('index.html', title = title, quote = quote)


@main.route('/blog/<int:id>')
def blog(id):
    '''
    view blog page function that will return the blog item
    '''
    # blog = get_blog
    return render_template('blog.html', blog_id = id)


@main.route('/blog/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    form = CommentForm()

    return render_template('new_comment.html', form = form)
 