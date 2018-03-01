from pos import Pos
from trip import Trip


class Car:
    def __init__(self, map):
        self.trips = []
        self.start_pos = Pos(0, 0)
        self.map = map

    def add_trip(self, trip):
        self.trips += [trip]

    def can_add_trip(self, trip):
        if len(self.trips) == 0:
            return True

        trip_list = self.valid_trip_list()
        return False

    def valid_trip_list(self):
        total_steps = 0
        current_pos = self.start_pos
        for scheduled_trip in self.trips:
            total_steps += current_pos.distance_to(scheduled_trip.start_pos)
            if total_steps > scheduled_trip.latest_start:
                return False
            total_steps += scheduled_trip.start_pos.distance_to(scheduled_trip.end_pos)
            if total_steps > self.map.total_time:
                return False
            current_pos = scheduled_trip.end_pos
        return True

    def all_trips_steps(self):
        total_steps = 0
        current_pos = self.start_pos
        for scheduled_trip in self.trips:
            total_steps += Trip(current_pos, scheduled_trip.start_pos).duration() + scheduled_trip.duration
            current_pos = scheduled_trip.end_pos

        return total_steps
