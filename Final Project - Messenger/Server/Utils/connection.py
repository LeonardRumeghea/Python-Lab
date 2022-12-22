class Connection:
    '''
        This class represents a connection to the server. It contains the username of the user that is connected, 
        the address of the user and the connection object.
    '''
    def __init__(self, username, addr, conn):
        '''
            Initializes the object with the username, address and connection object.

            :param username: The username of the user.
            :param addr: The address of the user.
            :param conn: The connection object.
        '''
        self.username = username
        self.addr = addr
        self.conn = conn

    def __str__(self):
        '''
            Returns a string representation of the object.
        '''
        return '{}: {} {}'.format(self.user.username, self.addr, self.conn)