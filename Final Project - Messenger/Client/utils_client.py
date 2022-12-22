import socket
from cryptography.fernet import Fernet
from CONSTANTS import *
import json
from message import Message

_cipher_suite = Fernet(KEY)

'''
    This file contains all the functions used in the client side of the application. 
'''

def send(socket, msg):
    '''
        Sends a message to the server. Message is encrypted before sending. We send the length of the message first,
        then the message itself.
        Encryption is done using the Fernet algorithm. Fernet uses AES in CBC mode with a 128-bit key for encryption.
        It is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet takes a 
        secret key and uses it to both encrypt data and verify that an encrypted message hasn't been tampered with.

        :param socket: The socket used to send the message.
        :param msg: The message to send.

        :return: Nothing.
    '''

    message = _cipher_suite.encrypt(msg.encode(FORMAT)).decode(FORMAT)

    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    socket.send(send_length)
    socket.send(message.encode(FORMAT))

def receive(socket):
    '''
        Receives a message from the server. Message is decrypted after receiving. We receive the length of the 
        message first, then the message itself.

        :param socket: The socket used to receive the message.

        :return: The decrypted message.
    '''

    try:
        msg_length = socket.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = socket.recv(msg_length).decode(FORMAT)
            return _cipher_suite.decrypt(msg.encode(FORMAT)).decode(FORMAT)

    except Exception as e:
        print(f'\tError: {e}\n')

def login_function(socket, username, password):
    '''
        Sends a login request to the server. The server will check if the username and password are correct.

        :param socket: The socket used to send the message.
        :param username: The username of the user.
        :param password: The password of the user.

        :return: True if the login was successful, False otherwise.
    '''
    send(socket, f'login {username} {password}')
    return receive(socket) == LOGIN_SUCCESS

def register_function(socket, username, password):
    '''
        Sends a register request to the server. The server will check if the username is already taken.

        :param socket: The socket used to send the message.
        :param username: The username of the user.
        :param password: The password of the user.

        :return: True if the register was successful, False otherwise.
    '''
    send(socket, f'register {username} {password}')
    return receive(socket) == REGISTER_SUCCESS

def send_message(socket, sender, receiver, content, image=NO_IMAGE):
    '''	
        Sends a message serialized to the server. The server will check if the receiver exists.

        :param socket: The socket used to send the message.
        :param sender: The sender of the message.
        :param receiver: The receiver of the message.
        :param content: The content of the message.
        :param image: The image of the message. Is optional.

        :return: True if the message was sent successfully, False otherwise.
    '''
    msg = serialize_message(Message(sender, receiver, emoji_translator(content), image))

    send(socket, f'send {msg}')

    return receive(socket) == SEND_SUCCESS

def load_inbox(socket):
    '''
        Loads the inbox of the user. The server will send the messages from the inbox.

        :param socket: The socket used to send the message.

        :return: The list of messages from the inbox.
    '''

    send(socket, 'inbox')
    response = receive(socket)
    return deserializable_messages(response)

def load_outbox(socket):
    '''
        Loads the outbox of the user. The server will send the messages from the outbox.

        :param socket: The socket used to send the message.

        :return: The list of messages from the outbox.
    '''

    send(socket, 'outbox')
    response = receive(socket)
    return deserializable_messages(response)

def close_connection(socket):
    '''
        Closes the connection with the server.

        :param socket: The socket used to send the message.

        :return: Nothing.
    '''

    send(socket, 'EXIT')
    socket.close()

def deserializable_messages(msg_list_json):
    '''
        Deserializes a list of messages from json format to Message objects.

        :param msg_list_json: The list of messages in json format.

        :return: The list of messages in Message objects.
    '''

    return json.loads(msg_list_json, object_hook=lambda m: Message( m['sender'],  m['receiver'],  m['content'], m['image']))

def serializable_messages(msg_list):
    '''
        Serializes a list of messages from Message objects to json format.

        :param msg_list: The list of messages in Message objects.

        :return: The list of messages in json format.
    '''

    return json.dumps(msg_list, default=lambda m: m.__dict__, indent=4, sort_keys=True)

def serialize_message(msg_json):
    '''
        Serializes a message from Message object to json format.

        :param msg_json: The message in Message object.

        :return: The message in json format.
    '''

    return json.dumps(msg_json, default=lambda m: m.__dict__, indent=4, sort_keys=True)

def emoji_translator(message):
    '''
        Translates the symbols emojis from the message to the corresponding unicode.

        :param message: The message to translate.

        :return: The translated message.
    '''

    for emoji in EMOJIS:
        message = message.replace(emoji, EMOJIS[emoji])

    return message









