import json
from .CONSTANTS import *

class User:

    def __init__(self, username, password, logged_in=False):
        self.username = username
        self.logged_in = logged_in
        self.password = password

    def __str__(self):
        return f'Username: {self.username}, Password: {self.password}, Logged In: {self.logged_in}'

    def __repr__(self):
        return self.__str__()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)