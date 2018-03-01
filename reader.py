from map import Map
from pos import Pos
from trip import Trip


def read_file(filename):
    global map

    with open(filename) as f:
        lines = f.readlines()

        first_line = True

        for line in lines:
            elements = line.split(" ")
            int_elements = [int(el) for el in elements]

            if first_line:
                first_line = False
                map = Map(
                    int_elements[0],
                    int_elements[1],
                    int_elements[2],
                    int_elements[3],
                    int_elements[4],
                    int_elements[5]
                )

            else:
                trip = Trip(
                    Pos(int_elements[0], int_elements[1]),
                    Pos(int_elements[2], int_elements[3]),
                    int_elements[4],
                    int_elements[5]
                )
                map.add_trip(trip)

    return {'map': map}
