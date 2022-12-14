import socket
from cryptography.fernet import Fernet
from CONSTANTS import *
import json
from message import Message


_cipher_suite = Fernet(KEY)

def send(socket, msg):
    message = _cipher_suite.encrypt(msg.encode(FORMAT)).decode(FORMAT)

    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    socket.send(send_length)
    socket.send(message.encode(FORMAT))

def receive(socket):
    try:
        msg_length = socket.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = socket.recv(msg_length).decode(FORMAT)
            return _cipher_suite.decrypt(msg.encode(FORMAT)).decode(FORMAT)

    except Exception as e:
        print(f'\tError: {e}\n')

def login_function(socket, username, password):
    send(socket, f'login {username} {password}')
    response = receive(socket)
    print(response)
    if response == LOGIN_SUCCESS:
        return True
    else:
        return False

def register_function(socket, username, password):
    send(socket, f'register {username} {password}')
    response = receive(socket)
    print(response)
    if response == REGISTER_SUCCESS:
        return True
    else:
        return False

def send_message(socket, sender, receiver, content, image=NO_IMAGE):
    msg = serialize_message(Message(sender, receiver, content, image))

    send(socket, f'send {msg}')
    
    response = receive(socket)
    print(response)
    if response == SEND_SUCCESS:
        return True
    else:
        return False

def load_inbox(socket):
    send(socket, 'inbox')
    response = receive(socket)
    return deserializable_messages(response)

def load_outbox(socket):
    send(socket, 'outbox')
    response = receive(socket)
    return deserializable_messages(response)

def close_connection(socket):
    send(socket, 'EXIT')
    socket.close()

def deserializable_messages(msg_json):
    return json.loads(msg_json, object_hook=lambda m: Message( m['sender'],  m['receiver'],  m['content']))

def serializable_messages(msg_list):
    return json.dumps(msg_list, default=lambda m: m.__dict__, indent=4, sort_keys=True)

def serialize_message(msg):
    return json.dumps(msg, default=lambda m: m.__dict__, indent=4, sort_keys=True)