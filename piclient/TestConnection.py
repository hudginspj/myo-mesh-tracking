from TCPClient import TCPNode
import time


def vibrate():
    print("VIBRATING")

def main():
    # node0 = TCPNode(0, vibrate)
    # node1 = TCPNode(1, vibrate)
    node2 = TCPNode(2, vibrate)

    # node0.connect('localhost', 8000)
    # node1.connect('localhost', 8000)
    node2.connect('localhost', 8000)

    while True:
        #
        # node0.send(0, 50)
        # time.sleep(1)
        #
        # node1.send(0, 50)
        # time.sleep(1)

        node2.send(2, -20.5)
        time.sleep(1)


if __name__ == '__main__':
    main()