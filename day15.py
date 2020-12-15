from dataclasses import dataclass


def parse_input_file():
    with open("day15_data.txt", "r") as file:
        return [int(i) for i in file.read().split(',')]


@dataclass
class Number:
    prev: int
    last: int


def nth_elem(n):
    numbers = {}
    input = parse_input_file()
    last_num = 0
    for ix, num in enumerate(input):
        numbers[num] = Number(-1, ix)
        last_num = num
    start_ix = len(numbers)
    for current_ix in range(start_ix, n, 1):
        if numbers[last_num].prev == -1:
            last_num = 0
        else:
            last_num = numbers[last_num].last - numbers[last_num].prev
        if last_num not in numbers:
            numbers[last_num] = Number(-1, current_ix)
        numbers[last_num].prev = numbers[last_num].last
        numbers[last_num].last = current_ix
    return last_num


def nth_elem_hashmap(n):
    numbers = {}
    input = parse_input_file()
    last_num = 0
    for ix, num in enumerate(input):
        numbers[num] = [ix]
        last_num = num
    start_ix = len(numbers)
    for current_ix in range(start_ix, n, 1):
        if len(numbers[last_num]) == 1:
            last_num = 0
        else:
            last_num = numbers[last_num][-1] - numbers[last_num][-2]
        if last_num not in numbers:
            numbers[last_num] = [current_ix]
        numbers[last_num].append(current_ix)
    return last_num


### Part 1 ###
#print(nth_elem(2020))
print(nth_elem_hashmap(2020))

### Part 2 ###
#print(nth_elem(30000000))
print(nth_elem_hashmap(30000000))
