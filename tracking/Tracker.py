import random
from tracking.path import *
from tracking.equations import *
import time
STATUSES = ['good', 'offline', 'removed', 'out']
STAT_GOOD = 0
STAT_OFF = 1
STAT_REMOVED = 2
STAT_OUT = 3

TRACKER_TIMEOUT = 5

class Tracker(object):

    def __init__(self):
        self.node_statuses = [STAT_OFF, STAT_OFF, STAT_OFF, STAT_OFF, STAT_OFF]
        self.rssis = [-1000, -1000, -1000, -1000, -1000]
        self.distances = [None, None, None, None, None]
        self.status = 1
        self.sector = -1
        self.timeouts = []

        timeout = time.time() + 3600
        for i in range(5):
            self.timeouts.append(timeout)

    def check_timeouts(self):
        now = time.time()
        for i in range(5):
            if (now > self.timeouts[i]):
                self.distances[i] = None
                self.node_statuses[i] = STAT_OFF
                self.compute_status_and_sector()
        print("Chk tmt: now/stat/sec/dis", now, self.status, self.sector, self.distances)


    def respond_to_pi(self, node, status, rssi):
        # self.status = random.randint(0,3)
        # self.sector = random.randint(0,4)
        self.node_statuses[node] = status
        if status in [STAT_GOOD, STAT_REMOVED]:
            self.rssis[node] = rssi
            self.distances[node] = distance(node, rssi)
            self.timeouts[node] = time.time() + TRACKER_TIMEOUT
            print("New timeout", node, self.timeouts[node])
        else:
            self.rssis[node] = 10000
            self.distances[node] = None

        self.compute_status_and_sector()

        print("update", node, status, rssi)
        print("status/sector/distances", self.status, self.sector, self.distances)

        if self.status in [STAT_GOOD, STAT_OFF]:
            alarm = 0
        else:
            alarm = 1
        return alarm


    def compute_status_and_sector(self):

        if STAT_REMOVED in self.node_statuses:
            self.status = STAT_REMOVED
            return

        offline = True
        for stat in self.node_statuses:
            if stat != STAT_OFF:
                offline = False
        if offline:
            self.status = STAT_OFF
            return

        sector = sector_in_path(self.distances)

        if sector is not None:
            self.sector = sector
            self.status = STAT_GOOD
        else:
            self.status = STAT_OUT
            best_distance = 99999999
            for i in range(5):
                if self.distances[i] and self.distances[i] < best_distance:
                    self.sector = i
                    best_distance = self.distances[i]


