import math
from itertools import count


def parse_input_file():
    with open("day13_data.txt", "r") as file:
        return file.readlines()

def part_1():
    input = parse_input_file()
    arrival_time = int(input[0].strip())
    buses = input[1].split(',')
    next_bus_arrivals = []
    for bus in buses:
        if bus != 'x':
            next_bus_arrival = math.ceil(arrival_time / int(bus)) * int(bus)
            next_bus_arrivals.append((bus, next_bus_arrival))
    nearest_bus = min(next_bus_arrivals, key=lambda x: x[1])
    bus_number = int(nearest_bus[0])
    bus_arrival = nearest_bus[1]
    return bus_number * (bus_arrival - arrival_time)


def part_2():
    input = parse_input_file()
    buses = input[1].split(',')
    buses_without_blanks = [(offset, int(bus)) for offset, bus in enumerate(buses) if bus != 'x']
    buses_without_blanks.sort(key=lambda x: x[1], reverse=True)
    start_ts = 0
    step = 1
    for offset, bus_number in buses_without_blanks:
        for ts in count(start_ts, step):
            if (ts + offset) % bus_number == 0:
                start_ts = ts
                step *= bus_number
                break
    return start_ts


### Part 1 ###
print(part_1())

### Part 2 ###
print(part_2())