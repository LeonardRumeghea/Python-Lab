from .user import User
from .message import Message
from .CONSTANTS import *
import json
from cryptography.fernet import Fernet

_cipher_suite = Fernet(KEY)

def _load_users(decrypt=True):
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

    for user in known_users:
        user.username = _encrypt_string(user.username)
        user.password = _encrypt_string(user.password)
        user.logged_in = _encrypt_string(str(user.logged_in))

    with open(USERS_FILE, 'w') as f:
        json.dump(known_users, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def register_user(username, password):
    known_users = _load_users()
    for user in known_users:
        if user.username == username:
            return ALREADY_EXISTS

    known_users.append(User(username, password, True))
    _save_users(known_users)
    return SUCCESS

def login_user(username, password):

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
    known_users = _load_users()
    for user in known_users:
        if user.username == username:
            user.logged_in = False
            _save_users(known_users)
            return SUCCESS

    return INVALID_CREDENTIALS

def send_message(conn, msg, header=HEADER, format=FORMAT):

    print(f'\nSending message:\n\tDecrypted: {msg}')

    msg = _encrypt_string(msg).encode(format)

    print(f'\tEncrypted: {msg}\n')

    send_lenght = str(len(msg)).encode(format)
    send_lenght += b' ' * (header - len(send_lenght))
    conn.send(send_lenght)
    conn.send(msg)

def receive_message(conn, header=HEADER, format=FORMAT):

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
    return _cipher_suite.encrypt(message.encode(FORMAT)).decode(FORMAT)

def _decrypt_string(message):
    return _cipher_suite.decrypt(message.encode(FORMAT)).decode(FORMAT)

def load_messages(decrypt=True):
    with open(MESSAGES_FILE, 'r') as f:
        if f.read(1):
            f.seek(0)
            messages = json.load(f,
            object_hook=lambda m: Message(
                    _cipher_suite.decrypt(m['sender'].encode(FORMAT)).decode(FORMAT) if decrypt else m['sender'], 
                    _cipher_suite.decrypt(m['receiver'].encode(FORMAT)).decode(FORMAT) if decrypt else m['receiver'], 
                    _cipher_suite.decrypt(m['content'].encode(FORMAT)).decode(FORMAT) if decrypt else m['content'],
                )
            )
        else:
            messages = []

    return messages

def save_message(message):
    
    message.sender = _encrypt_string(message.sender)
    message.receiver = _encrypt_string(message.receiver)
    message.content = _encrypt_string(message.content)

    messages = load_messages(decrypt=False) + [message]
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def get_inbox_of(username):
    return [message for message in load_messages() if message.receiver == username]

def get_outbox_of(username):
    return [message for message in load_messages() if message.sender == username]

def format_messages(messages):
    return '\n'.join([f'{message.sender} -> {message.receiver}: {message.content}' for message in messages])







