import socket
import threading
from Utils.CONSTANTS import *
from Utils.utils_server import *
from Utils.connection import *
from Utils.commands import *

PORT = 4000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

def disconnect_user(connected_user):
    logout_user(connected_user.username)
    connected_user.conn.close()
    return True

def chat_mode(connected_user):

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

            elif msg[0].lower() == HELP_COMMAND:
                help_command(connected_user.conn)
            
            else:
                send_message(connected_user.conn, 'Wrong command')

        except Exception as e:
            print(f'Error: {e}')
            disconnect_user(connected_user)
            break

def authenticate(addr, conn):
    print('Authenticating', addr)
    
    while True:
        try:
            msg = receive_message(conn)

            if msg is None:
                break

            print(f'[{addr}] {msg}')

            if msg.lower() == HELP_COMMAND:
                help_command(conn)

            elif msg == DISCONNECT_COOMAND:
                print('Disconnected', addr)
                conn.close()
                break

            else:
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

    server_socket.listen()
    print('Server started on ', IP)
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=authenticate, args=(addr, conn))
        thread.start()
        print('Active connections:', threading.active_count() - 1)

print('Starting server...')
start()

