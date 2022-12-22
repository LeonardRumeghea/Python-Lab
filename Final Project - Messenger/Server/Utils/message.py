import json

class Message:
    '''
        Represents a message sent between two users.
    '''
    def __init__(self, sender, receiver, content, image=None):
        '''
            Initializes the object with the given parameters. The image parameter is optional.

            :param sender: The username of the sender.
            :param receiver: The username of the receiver.
            :param content: The content of the message.
            :param image: The image of the message. It is optional.
        '''
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.image = image

    def toJSON(self):
        '''
            Return a JSON representation of the object.
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        '''
            Returns a string representation of the object.
        '''
        return f'{self.sender} -> {self.receiver}: {self.content} - Image: {self.image}'