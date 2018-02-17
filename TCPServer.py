
import threading
from socket import *

class TCPServer(object):

    def __init__(self, host='localhost', port=8000):

        print("[+] Initializing Communication")

        self.on_arm = [0, 0, 0, 0, 0]
        self.rssi = [0, 0, 0, 0, 0]
        self.host = host
        self.port = port

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))

        connection_thread = threading.Thread(target=self.connect)
        connection_thread.setDaemon(True)
        connection_thread.start()

        connection_thread.join()

    def connect(self):
        self.server.listen(10)
        print("[+] Listening on port {}".format(self.port))

        while True:
            client, address = self.server.accept()
            #print "[+] Connection successful from " + address 
            
            client_thread = threading.Thread(target=self.start, args=(client,))
            client_thread.start()

    def start(self, client):
        while True:
            data = client.recv(4096)
            if not data:
                break

            data_list = data.decode().split(' ')

            self.on_arm[int(data_list[0])] = int(data_list[1])
            self.rssi[int(data_list[0])] = int(data_list[2])

            print(self.on_arm) 
            print(self.rssi)

    def close(self):
        self.server.close()