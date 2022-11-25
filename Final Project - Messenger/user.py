class User:
    def __init__(self, name, addr, conn):
        self.name = name
        self.addr = addr
        self.conn = conn

    def __str__(self):
        return '{}: {} {}'.format(self.name, self.addr, self.conn)

    def __repr__(self):
        return self.__str__()