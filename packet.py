import time


class Packet:
    def __init__(self, data, acked, send_time):
        self.data = data
        self.acked = acked
        self.send_time = send_time

    def was_sent(self):
        return self.send_time is not None




# returns the current time since the epcoh in ms
def now():
    return int(time.time() * 1000)


