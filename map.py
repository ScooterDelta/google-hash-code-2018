from car import Car


class Map:
    def __init__(self, rows, columns, cars, totalRides, bonus, totalTime):
        self.rows = rows
        self.columns = columns
        self.cars = [Car() for _ in range(cars)]
        self.totalRides = totalRides
        self.bonus = bonus
        self.totalTime = totalTime
        self.trips = []

    def add_trip(self, trip):
        self.trips += [trip]
