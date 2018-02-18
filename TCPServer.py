
import threading
from socket import socket, AF_INET, SOCK_STREAM
import time
from tracking.Tracker import *


class TCPServer(object):

    def __init__(self, host='0.0.0.0', port=8000):

        print("[+] Initializing Communication")

        self.status = [-1, -1, -1, -1, -1]
        self.rssi = [0, 0, 0, 0, 0]
        self.host = host
        self.port = port

        self.server = None

        self.tracker = Tracker()

        self.connection_thread = threading.Thread(target=self.connect)
        self.connection_thread.start()

        self.to_loop = threading.Thread(target=self.timeout_loop)
        self.to_loop.start()

        # self.connection_thread.join()

    def connect(self):
        # print('waiting')
        # time.sleep(3)  # TODO prevents overwriting of flask socket?
        print("[+] Mesh server listening on port {}".format(self.port))
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))

        self.server.listen(10)

        while True:
            client, address = self.server.accept()
            print("[+] Connection successful from {0}".format(address)) 
            
            client_thread = threading.Thread(target=self.start, args=(client,))
            client_thread.start()



    def timeout_loop(self):
        while True:
            self.tracker.check_timeouts()
            time.sleep(1)


    def start(self, client):
        while True:
            data = client.recv(4096)
            if not data:
                break

            data_list = data.decode().split(' ')

            # self.status[int(data_list[0])] = int(data_list[1])
            # self.rssi[int(data_list[0])] = int(data_list[2])
            node = int(data_list[0])
            status = int(data_list[1])
            rssi = float(data_list[2])

            print(node, status, rssi)

            alarm = self.tracker.respond_to_pi(node, status, rssi)
            # Sends an alert randomly for now
            client.send(str(alarm).encode())

        client.close()


    def close(self):
        self.server.close()


