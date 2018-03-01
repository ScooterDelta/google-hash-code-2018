class Trip:
    def __init__(self, start_pos, end_pos, earliest_start, latest_end):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.earliest_start = earliest_start

        self.latest_end = latest_end
        self.latest_start = latest_end - self.distance

    def distance(self):
        NotImplemented

    def duration(self):
        return self.distance()
