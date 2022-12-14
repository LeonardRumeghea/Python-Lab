class Message:
    def __init__(self, from_user, to_user, subject, content, image = None):
        self.from_user = from_user
        self.to_user = to_user
        self.subject = subject
        self.content = content
        self.image = image