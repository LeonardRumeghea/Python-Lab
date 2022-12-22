import json
from .CONSTANTS import *

class User:
    '''
        Represents a user. It contains the username, password and a boolean that indicates if the user is logged 
        in or not.
    '''

    def __init__(self, username, password, logged_in=False):
        '''
            Initializes the object with the given parameters.

            :param username: The username of the user.
            :param password: The password of the user.
            :param logged_in: A boolean that indicates if the user is logged in or not.
        '''
        self.username = username
        self.logged_in = logged_in
        self.password = password

    def __str__(self):
        '''
            Returns a string representation of the object.
        '''
        return f'Username: {self.username}, Password: {self.password}, Logged In: {self.logged_in}'
    
    def toJSON(self):
        '''
            Return a JSON representation of the object.
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)