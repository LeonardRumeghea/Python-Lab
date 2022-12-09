# from user import User

class Connection:
    def __init__(self, username, addr, conn):
        self.username = username
        self.addr = addr
        self.conn = conn

    def __str__(self):
        return '{}: {} {}'.format(self.user.username, self.addr, self.conn)