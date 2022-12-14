import json

class Message:
    def __init__(self, sender, receiver, content, image=None):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.image = image

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def __str__(self):
        return f'Sender: {self.sender} - Receiver: {self.receiver} - Content: {self.content} - Image: {self.image}'

    def __repr__(self):
        return f'Message({self.sender}, {self.receiver}, {self.content})'