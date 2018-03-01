from trip import Trip

class Car:
  def __init__(self, start_pos):
    self.trips = []
    self.start_pos = start_pos
    self.time
    self.score_calc

  def add_trip(self, trip):
    self.trips += [trip]

  def can_add_trip(trip):
    if len(self.trips) == 0:
      return True
    else valid_trip_list(


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




