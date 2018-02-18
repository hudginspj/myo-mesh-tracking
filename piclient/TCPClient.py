
import time
import socket


class TCPNode(object):

    def __init__(self, node_id, alarm_callback):
        self.alarm_callback = alarm_callback
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        self.rssi = 0
        self.id = node_id
        self.host = None
        self.port = None

    def connect(self, host, port):
        self.host = host
        self.port = port

        while self.sock.connect_ex((host, port)):
            time.sleep(2)

    def send(self, status, rssi):
        try:
            self.sock.send("{} {} {}".format(self.id, status, rssi).encode())
            self.recv(1024)
        except socket.error:
            self.connect(self.host, self.port)

    def recv(self, rate):
        data = self.sock.recv(rate).decode()

        if data == "1":
            self.alarm_callback()



    def close(self):
        self.sock.close()


