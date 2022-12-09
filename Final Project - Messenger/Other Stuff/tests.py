from cryptography.fernet import Fernet

_cipher_suite = Fernet('k2B_PEFU4I8HJ9Q4kOBGlfqVZnU2UDUYlILOpfNjljA=')


FORMAT = 'utf-8'
HEADER = 128

def _decrypt_string(message):
    print(f'\t\t\tDecrypting: {message}')
    try:
        return _cipher_suite.decrypt(message.encode('utf-8')).decode('utf-8')
    except Exception as e:
        print(f'\t\t\tException: {e}')
        # return message

string = _cipher_suite.encrypt('Hello!'.encode('utf-8')).decode('utf-8')

# print(string)
# print(_decrypt_string('gAAAAABjku1gI0PoIiBsZ3WPJ6sPoMqThBdfoj0a39xKzZKTRFfRdFc1szYg1RZa=='))


def send(msg):
    print(f'msg = {msg}')
    message = _cipher_suite.encrypt(msg.encode(FORMAT)).decode(FORMAT)
    print(f'message = {message}')
    
    msg_length = len(message)
    print(f'msg_length = {msg_length}')

    send_length = str(msg_length).encode(FORMAT)    
    print(f'send_length = {send_length}')
    
    send_length += b' ' * (HEADER - len(send_length))
    print(f'send_length = {send_length}')
    
    print(f'send_length = {_cipher_suite.encrypt(send_length)}')

    print(f'send_length decrypted = {_decrypt_string(_cipher_suite.encrypt(send_length).decode(FORMAT))}')

    print(f'message = {message.encode(FORMAT)}')
    # client_socket.send(_cipher_suite.encrypt(send_length))
    # client_socket.send(message.encode(FORMAT))

# send('Hello!')

print(_decrypt_string(b'gAAAAABjkujEJLI_mKGQCPNKH46HfXTjZiJYE4RKwtE8cBKxhM89Cz8-ip7-wvi42pUabzFRCgSBLKtaVzKWiPR5Y-CSup2lFQ=='.decode(FORMAT)))


















# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# Fernet uses: AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding
# Key is 32 url-safe base64-encoded bytes

# print('Key: ', key.decode('utf-8'))

# cipher_suite = Fernet(key)

# text = 'Hello!'
# print('1. ', text)

# encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
# print('2. ', encoded_text)

# decoded_text = cipher_suite.decrypt(encoded_text)
# print('5. ', decoded_text.decode('utf-8'))

# import time
# for x in range (0,5):  
#     b = "Loading" + "." * x
#     print (b, end="\r")
#     time.sleep(1)

# import json
# from user import User

# usr1 = User('admin', 'admin')
# usr2 = User('user', 'user')
# usr3 = User('guest', 'guest')

# known_users = [usr1, usr2, usr3]

# with open('users.json', 'w') as f:
#     json_string = json.dump(known_users, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)
#     print(json_string)

# with open('users.json', 'r') as f:
#     known_users_json = json.load(f)


# known_users = []
# for user in known_users_json:
#     known_users.append(User(user['username'], user['password']))

# print(*known_users, sep='\n')