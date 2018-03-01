def write_cars(filename, cars):
    file = open(filename, 'w')

    for car in cars:
        file.write(car.get_trip_string() + '\n')

    file.close()
