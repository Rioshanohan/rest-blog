class Post:
    def __init__(self, id, title, content, timestamp):
        self.id = id
        self.content = content
        self.title = title
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
                'id': self.id,
                'title': self.title,
                'content': self.content,
                'timestamp': self.timestamp
                }
