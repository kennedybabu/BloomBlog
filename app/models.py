class Quote:
    '''
    Quote class to define Quote objects
    '''

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote


class Comment:
    all_comments = []

    def __init__(self, id, blog_id, comment):
        self.id = id
        self.blog = blog_id
        self.comment = comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls, id):

        response = []

        for comment in cls.all_comments:
            if Comment.blog_id == id:
                response.append(comment)

        return response


class Blog:
    
    all_blogs=[]

    def __init__(self, id, title, author, description):
        self.id = id
        self.title = title
        self.author = author
        self.description = description

    def save_blogs(self):
        Blog.all_blogs.append(self)

    @classmethod
    def get_blogs(cls, id):

        response =[]

        for blog in cls.all_blogs:
            if Blog.blog_id == id:
                response.append(blog)
        return response
