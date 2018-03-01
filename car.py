from copy import deepcopy

from pos import Pos


class Car:
    def __init__(self):
        self.trips = []
        self.start_pos = Pos(0, 0)

    def add_trip(self, trip):
        if len(self.trips) == 0:
            self.trips = [trip]
            return True
        else:
            for i in range(len(self.trips) + 1):
                trips = deepcopy(self.trips)
                trips.insert(i, trip)
                if self.valid_trip_list(trips):
                    self.trips = trips
                    return True
            return False

    def valid_trip_list(self, trips):
        total_steps = 0
        current_pos = self.start_pos
        for scheduled_trip in trips:
            total_steps += current_pos.distance_to(scheduled_trip.start_pos)
            if total_steps > scheduled_trip.latest_start:
                return False
            total_steps += scheduled_trip.start_pos.distance_to(scheduled_trip.end_pos)
            if total_steps > self.map.total_time:
                return False
            current_pos = scheduled_trip.end_pos
        return True
