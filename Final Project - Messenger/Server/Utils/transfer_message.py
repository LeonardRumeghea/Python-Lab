class Transfer_Message:
    def __init__(self, from_user, to_user, content, public, image = None):
        self.from_user = from_user
        self.to_user = to_user
        self.content = content
        self.public = public
        self.image = image

    def __str__(self):
        type = '[G] ' if self.public else '[P] '
