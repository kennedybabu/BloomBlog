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
