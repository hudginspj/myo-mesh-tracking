
import time
import socket


class TCPNode(object):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rssi = 0

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, node_id, connected, rssi):
        self.sock.send("{} {} {}".format(node_id, connected, rssi).encode())

    def close(self):
        self.sock.close()

