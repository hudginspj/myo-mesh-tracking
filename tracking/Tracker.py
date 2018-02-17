import random

STATUSES = ['good', 'offline', 'removed', 'out']
STAT_GOOD = 0
STAT_OFF = 1
STAT_REMOVED = 2
STAT_OUT = 3

class Tracker(object):

    def __init__(self):
        self.node_statuses = [-1, -1, -1, -1, -1]
        self.rssis = [-1000, -1000, -1000, -1000, -1000]
        self.distances = [None, None, None, None, None]
        self.status = 1
        self.sector = -1


    def respond_to_pi(self, node, status, rssi):
        # self.status = random.randint(0,3)
        # self.sector = random.randint(0,4)
        self.node_statuses[node] = status
        if status in [STAT_GOOD, STAT_REMOVED]:
            self.rssis[node] = rssi



        if self.status == 0:
            alarm = 0
        else:
            alarm = 1
        return alarm

