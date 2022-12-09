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

connected_users = []

def disconnect_user(connected_user):
    result = logout_user(connected_user.username)

    if result != SUCCESS:
        return False

    send_message(connected_user.conn, DISCONNECT_COOMAND)
    connected_user.conn.close()
    connected_users.remove(connected_user)
    return True

def chat_mode(connected_user):

    print(f'Chat mode: {connected_user.username}')

    while True:
        try:
            msg = receive_message(connected_user.conn)

            if msg is None or msg == DISCONNECT_COOMAND:
                if disconnect_user(connected_user):
                    break
                else:
                    continue

            msg = msg.split(' ', 1)
            
            if msg[0].lower() == SEND_COMMAND:
                send_command(connected_user, msg[1], connected_users)
            
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

            if msg.lower() == HELP_COMMAND:
                help_command(conn)

            elif msg.lower() == DISCONNECT_COOMAND:
                send_message(conn, DISCONNECT_COOMAND)
                print('Disconnected', addr)
                conn.close()
                break

            msg = msg.strip().split(' ')

            if len(msg) != 3:
                send_message(conn, 'Wrong format')
                continue

            print(msg[0])
            
            if msg[0].lower() == LOGIN_COMMAND:

                result = login_command(msg[1], msg[2], addr, conn)

                if result is not None:
                    connected_users.append(result)
                    thread = threading.Thread(target=chat_mode, args=(result,))
                    thread.start()
                    break
                
            elif msg[0].lower() == REGISTER_COMMAND:

                result = register_command(msg[1], msg[2], addr, conn)

                if result is not None:
                    connected_users.append(result)
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

