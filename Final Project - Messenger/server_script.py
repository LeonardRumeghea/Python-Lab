import socket
from user import User
import threading

PORT = 4000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

connected_users = []


def handle_client(user):
    print('New connection from', user.addr)
    connected = True
    while connected:
        try:
            msg = user.conn.recv(1024)
            if msg:
                print('Message received from', user.addr, ':', msg.decode('utf-8'))
                if msg.decode('utf-8') == DISCONNECT_MESSAGE:
                    connected = False
                    user.conn.close()
                    connected_users.remove(user)
                    break
                else:
                    msg = '{}: {}'.format(user.name, msg.decode('utf-8')).encode('utf-8')
                    for usr in connected_users:
                        if usr != user:
                            usr.conn.send(msg) 
            else:
                connected = False
                user.conn.close()
                connected_users.remove(user)
                break

        except Exception as e:
            print('Error: ', e)
            connected = False
            user.conn.close()
            break


def start():
    server_socket.listen()
    print('Server started on', IP)
    while True:
        conn, addr = server_socket.accept()
        name = conn.recv(1024).decode('utf-8')
        user = User(name=name, addr=addr, conn=conn)
        connected_users.append(user)
        print('Connected users:', connected_users)
        thread = threading.Thread(target=handle_client, args=(user,))
        thread.start()
        print('Active connections:', threading.active_count() - 1)


print('Starting server...')
start()