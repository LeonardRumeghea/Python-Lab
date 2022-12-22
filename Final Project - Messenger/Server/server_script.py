import socket
import threading
from Utils.CONSTANTS import *
from Utils.utils_server import *
from Utils.connection import *
from Utils.commands import *

'''
    Server script for the chat application using TCP sockets and multithreading. The server is able to handle 
    multiple clients at the same time. The server is able to send and receive messages from the clients.
'''

PORT = 4000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

def disconnect_user(connected_user):
    '''
        Disconnects the user from the server. 

        connected_user: The user to be disconnected.
    '''
    logout_user(connected_user.username)
    connected_user.conn.close()

def chat_mode(connected_user):
    '''
        The chat mode of the server. The server is able to send and receive messages from the client. 

        connected_user: The user that is connected to the server.

        If the message is None or the message is the disconnect command, the user is disconnected from the server.

        User have several commands available:

            send <user> <json_message>: Sends a message to another user.
            inbox: Shows the messages received by the user.
            outbox: Shows the messages sent by the user.
            exit: Disconnects the user from the server.
    
    '''

    print(f'Chat mode: {connected_user.username}')

    while True:
        try:
            msg = receive_message(connected_user.conn)

            print(f'[{connected_user.username}] : {msg}')

            if msg is None or msg == DISCONNECT_COOMAND:
                disconnect_user(connected_user)

            msg = msg.strip().split(' ', 1)
            print(msg)

            if msg[0].lower() == SEND_COMMAND:
                send_command(connected_user.conn, msg[1])
            
            elif msg[0].lower() == INBOX_COMMAND:
                inbox_command(connected_user)
            
            elif msg[0].lower() == OUTBOX_COMMAND:
                outbox_command(connected_user)
            
            else:
                send_message(connected_user.conn, 'Wrong command')

        except Exception as e:
            print(f'Error: {e}')
            disconnect_user(connected_user)
            break

def authenticate(addr, conn):
    '''
        Authenticates the user. The user is able to login or register. After the user is authenticated, the chat 
        mode is started.

        addr: The address of the user.
        conn: The connection of the user.

        The user have some commands available. 

        login <username> <password>: The user is able to login to the server using the username and the 
        password.
        register <username> <password>: The user is able to register to the server using the username and
        the password.
        EXIT: The user is able to disconnect from the server.
    '''

    print('Authenticating', addr)
    
    while True:
        try:
            msg = receive_message(conn)

            if msg is None:
                break

            print(f'[{addr}] {msg}')

            if msg == DISCONNECT_COOMAND:
                print('Disconnected', addr)
                conn.close()
                break

            msg = msg.strip().split(' ')

            if len(msg) != 3:
                send_message(conn, 'Wrong format')
                continue

            if msg[0].lower() == LOGIN_COMMAND:

                result = login_command(msg[1], msg[2], addr, conn)

                if result is not None:
                    thread = threading.Thread(target=chat_mode, args=(result,))
                    thread.start()
                    break
                
            elif msg[0].lower() == REGISTER_COMMAND:

                result = register_command(msg[1], msg[2], addr, conn)

                if result is not None:
                    thread = threading.Thread(target=chat_mode, args=(result,))
                    thread.start()
                    break

            else:
                send_message(conn, 'Wrong command')
                print('Wrong command')

        except Exception as e:
            print('Error: ', e)
            break

def start():
    '''
        Starts the server. The server is able to handle multiple clients at the same time. He waits for the clients
        to connect to the server and then starts a new thread for each of them.
    '''

    server_socket.listen()
    print('Server started on ', IP)
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=authenticate, args=(addr, conn))
        thread.start()
        print('Active connections:', threading.active_count() - 1)

print('Starting server...')
start()

