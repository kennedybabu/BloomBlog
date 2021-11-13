from flask import render_template
from app import app


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    '''
    view blog page function that will return the blog item
    '''
    return render_template('blog.html', blog_id = blog_id)