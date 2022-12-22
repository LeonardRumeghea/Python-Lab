from Utils.user import User
from Utils.message import Message
from Utils.CONSTANTS import *
import json
from cryptography.fernet import Fernet

_cipher_suite = Fernet(KEY)

'''
    This file contains the functions that are used by the server.
'''

def _load_users(decrypt=True):
    '''
    Loads the users from the USERS_FILE and returns a list of User objects.
    If decrypt is True, the usernames and passwords will be decrypted.  
    :param decrypt: Whether or not to decrypt the usernames and passwords. Default is True.
    :return: A list of User objects.
    '''
    with open(USERS_FILE, 'r') as f:
        if f.read(1):
            f.seek(0)
            known_users = json.load(f, 
                object_hook=lambda d: User(
                    _decrypt_string(d['username']) if decrypt else d['username'],
                    _decrypt_string(d['password']) if decrypt else d['password'],
                    _decrypt_string(d['logged_in']) if decrypt else d['logged_in']
                    )
                )
        else:
            known_users = []

    return known_users

def _save_users(known_users):
    '''
    Saves the users to the USERS_FILE. The usernames, passwords and logged_in status will be encrypted. 

    :param known_users: A list of User objects.
    :return: Nothing.
    '''

    for user in known_users:
        user.username = _encrypt_string(user.username)
        user.password = _encrypt_string(user.password)
        user.logged_in = _encrypt_string(str(user.logged_in))

    with open(USERS_FILE, 'w') as f:
        json.dump(known_users, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def register_user(username, password):
    '''
    Registers a new user to system. Will also save the user encrypted to the USERS_FILE.

    :param username: The username of the user.
    :param password: The password of the user.

    :return: SUCCESS if the user was registered successfully.
    :return: ALREADY_EXISTS if the username is already taken.
    '''
    known_users = _load_users()
    for user in known_users:
        if user.username == username:
            return ALREADY_EXISTS

    known_users.append(User(username, password, True))
    _save_users(known_users)
    return SUCCESS

def login_user(username, password):
    '''
    Logins a user to the system. Will also save the user encrypted to the USERS_FILE.

    :param username: The username of the user.
    :param password: The password of the user.

    :return: SUCCESS if the user was logged in successfully.
    :return: INVALID_CREDENTIALS if the username or password is incorrect.
    :return: ALREADY_LOGGED_IN if the user is already logged in.
    '''

    known_users = _load_users()
    for user in known_users:
        if user.username == username and user.password == password:
            if user.logged_in == 'True':
                return ALREADY_LOGGED_IN
            user.logged_in = True
            _save_users(known_users)
            return SUCCESS

    return INVALID_CREDENTIALS

def logout_user(username):
    '''
    Logs out a user.  Will set the logged_in attribute to False for the user in the USERS_FILE.

    :param username: The username of the user.

    :return: Nothing.
    '''
    known_users = _load_users()
    for user in known_users:
        if user.username == username:
            user.logged_in = False
            _save_users(known_users)
            return

def send_message(conn, msg, header=HEADER, format=FORMAT):
    """
    Sends a message to a client. Before transmission, the message will be encrypted. The message's length
    will be transmitted first, then the message itself. Encryption is done using the Fernet algorithm from
    the cryptography library. Fernet uses AES in CBC mode with a 128-bit key for encryption.

    :param conn: The connection to the client.
    :param msg: The message to send.
    :param header: The length of the message's length. Default is 256.
    :param format: The format of the message. Default is 'utf-8'.

    :return: Nothing.
    """

    print(f'\nSending message:\n\tDecrypted: {msg}')

    msg = _encrypt_string(msg).encode(format)

    print(f'\tEncrypted: {msg}\n')

    send_lenght = str(len(msg)).encode(format)
    send_lenght += b' ' * (header - len(send_lenght))
    conn.send(send_lenght)
    conn.send(msg)

def receive_message(conn, header=HEADER, format=FORMAT):
    '''
    Receives a message from a client. After transmission, the message will be decrypted.
    The length of the message will be received before the message itself.

    :param conn: The connection to the client.
    :param header: The length of the message's length. Default is 256.
    :param format: The format of the message. Default is 'utf-8'.

    :return: The decrypted message.
    '''

    msg_lenght = conn.recv(header).decode(format)

    if msg_lenght:
        msg = conn.recv(int(msg_lenght))
        
        print(f'\nReceived message:\n\tEncrypted: {msg}')

        msg = _decrypt_string(msg.decode(format))

        print(f'\tDecrypted: {msg}\n')

        return msg
    else:
        return None

def _encrypt_string(message):
    '''
    Encrypts a string using the Fernet algorithm from the cryptography library and returns the encrypted string.

    :param message: The string to encrypt.

    :return: The encrypted string.
    '''
    return _cipher_suite.encrypt(message.encode(FORMAT)).decode(FORMAT)

def _decrypt_string(message):
    '''
    Decrypts a string using the Fernet algorithm from the cryptography library and returns the decrypted string.

    :param message: The string to decrypt.

    :return: The decrypted string.
    '''
    return _cipher_suite.decrypt(message.encode(FORMAT)).decode(FORMAT)

def load_messages(decrypt=True):
    '''
    Loads all messages from the MESSAGES_FILE. If decrypt is True, the messages will be decrypted before being returned.

    :param decrypt: Whether or not to decrypt the messages. Default is True.

    :return: A list of all messages.
    '''

    try:
        with open(MESSAGES_FILE, 'r') as f:
            if f.read(1):
                f.seek(0)
                messages = json.load(f,
                object_hook=lambda m: Message(
                        _cipher_suite.decrypt(m['sender'].encode(FORMAT)).decode(FORMAT) if decrypt else m['sender'], 
                        _cipher_suite.decrypt(m['receiver'].encode(FORMAT)).decode(FORMAT) if decrypt else m['receiver'], 
                        _cipher_suite.decrypt(m['content'].encode(FORMAT)).decode(FORMAT) if decrypt else m['content'],
                        _cipher_suite.decrypt(m['image'].encode(FORMAT)).decode(FORMAT) if decrypt else m['image']
                    )
                )
            else:
                messages = []

        return messages
    
    except Exception as e:
        print(e)
        return []

def save_message(message):
    '''
    Saves a message to the MESSAGES_FILE. The message will be encrypted before saving it.

    :param message: The message to save.

    :return: Nothing.
    '''
    
    message.sender = _encrypt_string(message.sender)
    message.receiver = _encrypt_string(message.receiver)
    message.content = _encrypt_string(message.content)
    message.image = _encrypt_string(message.image)

    messages = load_messages(decrypt=False) + [message]
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def get_inbox_of(username):
    '''
    Returns a list of messages that the user with the given username has received.

    :param username: The username of the user to get the inbox of.

    :return: A list of Message objects.
    '''

    return [message for message in load_messages() if message.receiver == username]

def get_outbox_of(username):
    '''
    Returns a list of messages that the user with the given username has sent.

    :param username: The username of the user to get the outbox of.

    :return: A list of Message objects.
    '''
    return [message for message in load_messages() if message.sender == username]

def get_usernames():

    '''
    Returns a list of usernames of all users saved in USERS_FILE.

    :return: A list of usernames.
    '''

    return [user.username for user in _load_users()]

def format_messages(messages):
    '''
    Formats a list of messages to be displayed in the terminal.

    :param messages: The list of messages to format.

    :return: A string containing the formatted messages.
    '''
    return '\n'.join([f'{message.sender} -> {message.receiver}: {message.content}' for message in messages])







