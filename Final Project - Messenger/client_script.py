import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4000
ADDR = (IP, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


def send(msg):
    # message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))
    # client_socket.send(send_length)
    client_socket.send(msg.encode(FORMAT))


def receive():
    while True:
        try:
            # msg_length = client_socket.recv(HEADER).decode(FORMAT)
            # if msg_length:
                # msg_length = int(msg_length)
            msg = client_socket.recv(1024).decode(FORMAT)
            print(msg)

        except Exception as e:
            print(e)
            break


def start():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    name = input('Enter your name: ')
    send(name)
    while True:
        msg = input()
        send(msg)

start()
