import os

with open('Other Stuff\\62464.jpg', 'rb') as f:
    poza = f.read()

with open('Other Stuff\\62465.jpg', 'wb') as f:
    f.write(poza)

















from cryptography.fernet import Fernet
# Fernet uses: AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding

key = Fernet.generate_key() # MmHYjUIqXpFHmU5mBFGK8Z5Q45rim9djVBl6GMumfgI=
# Key is 32 url-safe base64-encoded bytes

cipher_suite = Fernet(key)

text = 'Hello!' # Hello!
 
encoded_text = cipher_suite.encrypt(text.encode('utf-8')) # gAAAAABjkv4UUU_kpPaNc-h01qDEdfujMnHmd6l-Skhazkr4YotAhnPnoC3sczKgg2nbd0utWQPIPQZMeI6afGl95-R6j0cS7Q==

decoded_text = cipher_suite.decrypt(encoded_text) # Hello!

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