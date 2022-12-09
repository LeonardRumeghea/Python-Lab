import socket
import threading
from cryptography.fernet import Fernet

IP = socket.gethostbyname(socket.gethostname())
PORT = 4000
ADDR = (IP, PORT)
HEADER = 256
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'EXIT'

KEY = 'k2B_PEFU4I8HJ9Q4kOBGlfqVZnU2UDUYlILOpfNjljA='

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)
cipher_suite = Fernet(KEY)

def send(msg):
    message = cipher_suite.encrypt(msg.encode(FORMAT)).decode(FORMAT)
    
    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client_socket.send(send_length)
    client_socket.send(message.encode(FORMAT))

def receive():
    try:
        msg_length = client_socket.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client_socket.recv(msg_length).decode(FORMAT)
            return cipher_suite.decrypt(msg.encode(FORMAT)).decode(FORMAT)

    except Exception as e:
        print(f'\tError: {e}\n')
  
def handle_receive():
    while True:
        msg = receive()
        if msg == DISCONNECT_MESSAGE:
            print('Disconnected')
            break

        print(msg, end='\r')
        print('\r')

def handle_send():
    while True:
        msg = input()
        send(msg)
        if msg == DISCONNECT_MESSAGE:
            break

def login():

    print('\n\t-= Welcome! =-\n')
    print('---------------------------------------------------------')
    print('Please use one of the following commands to authenticate:')
    print('\t•LOGIN <username> <password>')
    print('\t•REGISTER <username> <password>')
    print('\t•EXIT - to exit the program')
    print('\t•HELP - to see the commands that you can use')
    print('---------------------------------------------------------')
    print('')

    while True:
        command = input('> ')

        if command == DISCONNECT_MESSAGE:
            return False 
        
        # client -> server -> client
        send(command)
        msg = receive()

        if msg == 'Logged in' or msg == 'Registered':
            print('Logged in')
            return True
        else:
            print(msg)

def start():

    logined = login()

    if logined:
        receive_thread = threading.Thread(target=handle_receive)
        receive_thread.start()

        send_thread = threading.Thread(target=handle_send)
        send_thread.start()
    
    else:
        client_socket.close()

start()
