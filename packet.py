import time


class Packet:
    def __init__(self, index, data, acked, send_time):
        self.index = index
        self.data = data
        self.acked = acked
        self.send_time = send_time

    def was_sent(self):
        return self.send_time is not None

    def in_transit(self):
        return self.was_sent() and not self.acked

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        return hash(self.index)

    def __lt__(self, other):
        return self.index < other.index



# returns the current time since the epcoh in ms
def now():
    return int(time.time() * 1000)
