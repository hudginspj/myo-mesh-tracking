
import time
import socket

class TCPNode(object):

    def __init__(self, node_id):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.node_id = node_id
        self.rssi = 0

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, node_id, connected, rssi):
        self.sock.send("%s %s %s" % (node_id, connected, rssi))

    def close(self):
        self.sock.close()

