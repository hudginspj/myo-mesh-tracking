
import threading
import socket

class TCPServer(object):

    def __init__(self, host='localhost', port=8000):

        print "[+] Initializing Communication" 

        self.on_arm = [0, 0, 0, 0, 0]
        self.rssi = [0, 0, 0, 0, 0]
        self.host = host
        self.port = port

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))

        connection_thread = threading.Thread(target=self.connect)
        connection_thread.start()

    def connect(self):
        self.server.listen(10)
        print "[+] Listening on port %s" % self.port

        while True:
            client, address = self.server.accept()
            print "[+] Connection successful from %s" % address 
            
            client_thread = threading.Thread(target=self.start, args=(client,))

    def close(self):
        self.server.close()