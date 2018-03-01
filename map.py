from car import Car


class Map:
    def __init__(self, rows, columns, cars, total_rides, bonus, total_time):
        self.rows = rows
        self.columns = columns
        self.cars = [Car() for _ in range(cars)]
        self.total_rides = total_rides
        self.bonus = bonus
        self.total_time = total_time
        self.trips = []

    def add_trip(self, trip):
        self.trips += [trip]

    def __str__(self):
        return "rows:" + str(self.rows) + " columns: " + str(self.columns) + " trips length: " + str(len(self.trips))
