'''
    This file contains all the constants used in the server.
'''

'''
    This are the constants used to send/receive messages from the client and encrypt/decrypt the messages.
'''
HEADER = 256
FORMAT = 'utf-8'
KEY = 'k2B_PEFU4I8HJ9Q4kOBGlfqVZnU2UDUYlILOpfNjljA='

'''
    This are the constants represents the location of the files used to store the messages and users.
'''
MESSAGES_FILE = './/Storage//messages.json'
USERS_FILE = './/Storage//users.json'	

'''
    This are the constants used to represent the commands used by the client.
'''
SEND_COMMAND = 'send'
INBOX_COMMAND = 'inbox'
OUTBOX_COMMAND = 'outbox'
REGISTER_COMMAND = 'register'
LOGIN_COMMAND = 'login'
DISCONNECT_COOMAND = 'EXIT'
HELP_COMMAND = 'help'

'''
    This are the constants used by functions to represent the status of the operation.
'''
INVALID_CREDENTIALS = 'invalid_credentials'
SUCCESS = 'success'
ALREADY_LOGGED_IN = 'already_logged_in'
ALREADY_EXISTS = 'already_exists'
LOGIN_SUCCESS = 'login success'
REGISTER_SUCCESS = 'register success'
SEND_SUCCESS = 'send success'
SEND_FAILURE = 'send failure'
NO_IMAGE = 'no image'
