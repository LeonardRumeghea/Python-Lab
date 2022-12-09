class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}: {self.content}'

    def __repr__(self):
        return f'Message({self.sender}, {self.receiver}, {self.content})'