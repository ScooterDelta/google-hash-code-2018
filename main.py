from reader import read_file
from writer import write_cars


def main():
    file_names = ['a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus']
    file_name = file_names[0]

    map = read_file('resources/' + file_name + '.in')
    map.distribute_trips()

    write_cars('results/' + file_name + '.out', map.cars)


if __name__ == "__main__":
    main()
