from TCPClient import TCPNode
import random
import time

def main():
    node0 = TCPNode()
    node1 = TCPNode()
    node2 = TCPNode()

    # node0.connect('172.29.46.213', 8000)
    node1.connect('localhost', 8000)
    node2.connect('localhost', 8000)

    while True:
        # node0.send(0, 1, 50)
        node1.send(1, 1, 50)
        node2.send(2, 1, 50)

        time.sleep(1)


if __name__ == '__main__':
    main()