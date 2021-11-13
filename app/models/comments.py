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