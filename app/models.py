from . import db
from datetime import  datetime

class Quote:
    '''
    Quote class to define Quote objects
    '''

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')
    comment = db.relationship('Comment', backref='author',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Comment {self.comment_content}'
 

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')


    def __repr__(self):
        return self.title
    
    

