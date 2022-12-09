from .utils_server import *
from .connection import *

def send_command(user, msg, connected_users):
    msg = msg.split(' ', 1)
    if len(msg) != 2:
        send_message(user.conn, 'Wrong format. Use: send <username> <message>')
        return

    for usr in connected_users:
        if usr.username == msg[0]:
            send_message(usr.conn, f'Message from {user.username}: {msg[1]}')
            save_message(Message(user.username, msg[0], msg[1]))
            send_message(user.conn, 'Message delivered!')
            break
    else:
        send_message(user.conn, 'Error: User not found')

def inbox_command(user):
    inbox = get_inbox_of(user.username)
    inbox = format_messages(inbox) if inbox is not [] else 'Empty'
    send_message(user.conn, f'\nInbox: \n{inbox}\n')	

def outbox_command(user):
    outbox = get_outbox_of(user.username)
    outbox = format_messages(outbox) if outbox is not [] else 'Empty'
    send_message(user.conn, f'\nOutbox: \n{outbox}')	

def help_command(conn):
    string_buffer = '\nCommands:\n'
    string_buffer += '\t•To Authenticate:\n'
    string_buffer += '\t\t•LOGIN <username> <password>\n'
    string_buffer += '\t\t•REGISTER <username> <password>\n'
    string_buffer += '\n\t•To Send Message:\n'
    string_buffer += '\t\t•SEND <username> <message>\n'
    string_buffer += '\n\t•To Check Your Messages:\n'
    string_buffer += '\t\t•INBOX\n'
    string_buffer += '\t\t•OUTBOX\n'
    string_buffer += '\n\t•To Exit:\n'
    string_buffer += '\t\t•EXIT\n'
    string_buffer += '\n\t•To Get Help:\n'
    string_buffer += '\t\t•HELP\n'

    send_message(conn, string_buffer)

def login_command(username, password, addr, conn):
    result = login_user(username, password)

    if result == SUCCESS:
        user_conn = Connection(username, addr, conn)
        send_message(conn, 'Logged in')
        print('Logged in')
        return user_conn

    elif result == ALREADY_LOGGED_IN:
        send_message(conn, 'User already logged in')
        print('User already logged in')
        
    else:
        send_message(conn, 'Wrong username or password')
        print('Wrong username or password')

    return None

def register_command(username, password, addr, conn):
    
    result = register_user(username, password)
                
    if result == SUCCESS:
        user_conn = Connection(username, addr, conn)
        send_message(conn, 'Registered')
        print('Registered')
        return user_conn

    elif result == ALREADY_EXISTS:
        send_message(conn, 'Username already exists')
        print('Username already exists')

    else:
        send_message(conn, 'Error')
        print('Error')

    return None











