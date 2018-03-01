class Trip:
  def __init__(self, start_x, start_y, end_x, end_y, earliest_start, latest_end)
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.earliest_start = earliest_start
    self.latest_end = latest_end

    self.latest_start = latest_end - self.distance

  def distance(self):

