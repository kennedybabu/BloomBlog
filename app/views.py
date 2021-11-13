from flask import render_template
from app import app
from .request import get_quotes


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quotes()
    title = 'Home, BlogBlossom'
    print(quote)
    return render_template('index.html', title = title, quote = quote)


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    '''
    view blog page function that will return the blog item
    '''
    return render_template('blog.html', blog_id = blog_id)