from .utils_server import *
from .connection import *

def send_command(conn, msg_json):
    msg = json.loads(msg_json, object_hook=lambda m: Message( m['sender'],  m['receiver'],  m['content']))
    if msg.image == 'null' or msg.image == None:
        msg.image = ''
    for username in get_usernames():
        if username == msg.receiver:
            save_message(Message(msg.sender, msg.receiver, msg.content, msg.image))
            send_message(conn, SEND_SUCCESS)
            break
    else:
        send_message(conn, SEND_FAILURE)

def inbox_command(user):
    inbox = get_inbox_of(user.username)
    send_message(user.conn, json.dumps(inbox, default=lambda o: o.__dict__, sort_keys=True, indent=4))	

def outbox_command(user):
    outbox = get_outbox_of(user.username)
    send_message(user.conn, json.dumps(outbox, default=lambda o: o.__dict__, sort_keys=True, indent=4))	

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
        send_message(conn, LOGIN_SUCCESS)
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
        send_message(conn, REGISTER_SUCCESS)
        print('Registered')
        return user_conn

    elif result == ALREADY_EXISTS:
        send_message(conn, 'Username already exists')
        print('Username already exists')

    else:
        send_message(conn, 'Error')
        print('Error')

    return None











