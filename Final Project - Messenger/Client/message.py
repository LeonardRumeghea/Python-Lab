import json

class Message:
    '''
        Message class. It contains the sender, receiver, content and image of the message. Is used to send messages 
        between users.
    '''
    def __init__(self, sender, receiver, content, image=None):
        '''
            Initializes the message object with the given parameters.

            :param sender: The sender of the message.
            :param receiver: The receiver of the message.
            :param content: The content of the message.
            :param image: The image of the message. Is optional.
        '''
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.image = image

    def toJSON(self):
        '''
            Returns the message as a JSON serialized.
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):
        '''
            Returns the message as a string.
        '''
        return f'Sender: {self.sender} - Receiver: {self.receiver} - Content: {self.content} - Image: {self.image}'