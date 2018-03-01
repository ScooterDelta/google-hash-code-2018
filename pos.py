class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance_to(self, pos):
    abs(self.x - pos.x) + abs(self.y - pos.y)
