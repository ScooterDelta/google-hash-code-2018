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
            number_trips = len(self.trips)
            for i in range(0, number_trips):
                prev_trip = self.trips[i]

                if i == 0:
                    time = self.start_pos.distance_to(trip.start_pos) + trip.start_pos.distance_to(trip.end_pos)
                    time += trip.end_pos.distance_to(prev_trip.start_pos)
                    if time < prev_trip.latest_start:
                        self.trips.insert(i, trip)
                        return True

                prev_trip_end = self.find_pref_trip_end(self.trips[0:i])
                if prev_trip_end + prev_trip.end_pos.distance_to(trip.start_pos) < trip.latest_start:
                    detour_distance = prev_trip.end_pos.distance_to(trip.start_pos)
                    detour_distance += trip.start_pos.distance_to(trip.end_pos)

                    if i + 1 < number_trips:
                        next_trip = self.trips[i + 1]
                        detour_distance += trip.end_pos.distance_to(next_trip.start_pos)

                        if prev_trip.latest_end + detour_distance <= next_trip.latest_start:
                            self.trips.insert(i + 1, trip)
                            return True

                    elif detour_distance < self.map.total_time:
                        self.trips.insert(i + 1, trip)
                        return True

            return False

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

    def find_pref_trip_end(self, trips):
        end_time = 0
        current_pos = self.start_pos
        for scheduled_trip in trips:
            end_time += current_pos.distance_to(scheduled_trip.start_pos)

            end_time = max(end_time, scheduled_trip.earliest_start)
            end_time += scheduled_trip.start_pos.distance_to(scheduled_trip.end_pos)
            current_pos = scheduled_trip.end_pos
        return end_time
