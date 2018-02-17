from TCPClient import TCPNode
import random
import time

def main():
    node0 = TCPNode(0)
    node1 = TCPNode(1)
    node2 = TCPNode(2)

    node0.connect('localhost', 8000)
    node1.connect('localhost', 8000)
    node2.connect('localhost', 8000)

    while True:
        node0.send(1, 50)
        node0.recv(1024)
        node1.send(1, 50)
        node1.recv(1024)
        node2.send(1, 50)
        node2.recv(1024)

        time.sleep(1)


if __name__ == '__main__':
    main()