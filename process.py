# Junnan Shimizu
# 2/17/22
# CS337ProjectOne
# CS337

class Process:
    def __init__(self, id, burst_time, arrival_time, priority):
        self.id = id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0

    def get_id(self):
        return self.id

    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, value):
        self.burst_time = value

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, value):
        self.arrival_time = value

    def get_priority(self):
        return self.priority

    def set_priority(self, value):
        self.priority = value

    def get_wait_time(self):
        return self.wait_time

    def set_wait_time(self, value):
        self.wait_time = value

    def get_turnaround_time(self):
        return self.turnaround_time

    def set_turnaround_time(self, value):
        self.turnaround_time = value

