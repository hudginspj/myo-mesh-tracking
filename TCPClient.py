
import time
import socket

class TCPNode(object):

    def __init__(self, node_id):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.node_id = node_id

    def connect(self, host, port):
        self.sock.connect((host, port))

        while True:
            sock.send("%s" % (self.node_id))
            time.sleep(0.1)

    def close(self)
        self.sock.close()
