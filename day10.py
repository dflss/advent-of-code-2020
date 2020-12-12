from collections import defaultdict


def parse_input_file():
    with open("day10_data.txt", "r") as file:
        lines = file.readlines()
    return [int(line) for line in lines]


### Part 1 ###
numbers = parse_input_file()
numbers.append(0)
numbers.sort()
numbers.append(numbers[-1] + 3)
jolts_1 = 0
jolts_3  = 0
prev = numbers[0]
for i in range(1, len(numbers), 1):
    if numbers[i] - prev == 1:
        jolts_1 += 1
    elif numbers[i] - prev == 3:
        jolts_3 += 1
    prev = numbers[i]
print(jolts_1 * jolts_3)


### Part 2 ###
possibilities = defaultdict(int)
possibilities[0] = 1
for num in numbers:
    for i in range(1, 4):
        next = num + i
        if next in numbers:
            possibilities[next] += possibilities[num]
print(possibilities[numbers[-1]])

