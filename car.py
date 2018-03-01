from copy import deepcopy

from pos import Pos


class Car:
    def __init__(self, map):
        self.trips = []
        self.start_pos = Pos(0, 0)
        self.map = map

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

    def calculate_score(self):
        total_steps = 0
        total_score = 0
        current_pos = self.start_pos
        for scheduled_trip in self.trips:
            total_steps += current_pos.distance_to(scheduled_trip.start_pos)
            if total_steps == scheduled_trip.earliest_start:
                total_score += self.map.bonus
            trip_distance = scheduled_trip.start_pos.distance_to(scheduled_trip.end_pos)
            total_steps += trip_distance
            total_score += trip_distance
            current_pos = scheduled_trip.end_pos
        return total_score

    def get_trip_string(self):
        string = str(len(self.trips))
        for trip in self.trips:
            string += " " + str(trip.index)
        return string
