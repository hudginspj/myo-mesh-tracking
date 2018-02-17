
import time
import socket

class TCPNode(object):

    def __init__(self, node_id):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rssi = 0
        self.id = node_id

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, connected, rssi):
        self.sock.send("{} {} {}".format(self.id, connected, rssi).encode())

    def recv(self, rate):
        data = self.sock.recv(rate).decode()

        if data == "1":
            self.alert()

    def alert(self):
        print("[!!!] ALARM SOUNDED:", self.id)

    def close(self):
        self.sock.close()


