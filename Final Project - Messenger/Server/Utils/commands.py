from .utils_server import *
from .connection import *

def send_command(conn, msg_json):
    '''
        This function is called when the client sends a SEND command. This will send a message to another user.
        If the user is not found, the client will be notified with a SEND_FAILURE message. Otherwise, the message 
        will be saved and the client will be notified with a SEND_SUCCESS message.

        :param conn: The connection to the client.
        :param msg_json: The message to send in JSON format.

        :return: None
    '''

    msg = json.loads(msg_json, object_hook=lambda m: Message( m['sender'],  m['receiver'],  m['content'], m['image']))
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
    '''
        This function is called when the client sends an INBOX command.
        It will get the inbox of the user and send it to the client as a JSON string.

        :param user: The user that sent the command. Is a Connection object.

        :return: None
    '''

    inbox = get_inbox_of(user.username)
    send_message(user.conn, json.dumps(inbox, default=lambda o: o.__dict__, sort_keys=True, indent=4))	

def outbox_command(user):
    '''
        This function is called when the client sends an OUTBOX command.
        It will get the outbox of the user and send it to the client as a JSON string.

        :param user: The user that sent the command. Is a Connection object.

        :return: None
    '''

    outbox = get_outbox_of(user.username)
    send_message(user.conn, json.dumps(outbox, default=lambda o: o.__dict__, sort_keys=True, indent=4))	

def help_command(conn):
    '''
        This function is called when the client sends a HELP command. It will send a list of commands to the client as string.

        :param conn: The connection to the client.

        :return: None
    '''

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
    '''
        This function is called when the client sends a LOGIN command. It will check if the user exists and if the password is correct. If the 
        user exists and the password is correct, it will send a LOGIN_SUCCESS message to the client. If the user is already logged in, it will 
        send a ALREADY_LOGGED_IN message to the client. Otherwise, it will send a WRONG_USERNAME_OR_PASSWORD message to the client.

        :param username: The username received from the user.
        :param password: The password received from the user.

        :return: The Connection object of the user if the login was successful, None otherwise.
    '''

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
    '''
        This function is called when the client sends a REGISTER command. It will check if the user exists. If the user does not exist, it will 
        send a REGISTER_SUCCESS message to the client and save the user. Otherwise, it will send a ALREADY_EXISTS message to the client.

        :param username: The username received from the user.
        :param password: The password received from the user.

        :return: The Connection object of the user if the registration was successful, None otherwise.
    '''
    
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











