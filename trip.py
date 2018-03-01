class Trip:
    def __init__(self, index, start_pos, end_pos, earliest_start, latest_end):
        self.index = index
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.earliest_start = earliest_start

        self.latest_end = latest_end
        self.latest_start = latest_end - start_pos.distance_to(end_pos)
