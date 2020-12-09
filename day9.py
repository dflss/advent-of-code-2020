PREAMBLE_LENGTH = 25


def is_correct(preamble_nums, number):
    for num1 in preamble_nums:
        for num2 in preamble_nums:
            if num1 + num2 == number:
                return True
    return False


def parse_input_file():
    with open("day9_data.txt", "r") as file:
        lines = file.readlines()
    return [int(line) for line in lines]


def find_first_incorrect_num(numbers, preamble_length):
    preamble_nums = [numbers[i] for i in range(preamble_length)]

    for index in range(preamble_length, len(numbers) - 1, 1):
        if not is_correct(preamble_nums, numbers[index]):
            return numbers[index]
        preamble_nums.remove(preamble_nums[0])
        preamble_nums.append(numbers[index])


def find_vuln(numbers, incorrect_num):
    last = 0
    current = 0
    sum = 0
    contiguous_set = []
    while current < len(numbers):
        sum += numbers[current]
        contiguous_set.append(numbers[current])
        if sum == incorrect_num:
            return max(contiguous_set) + min(contiguous_set)
        elif sum < incorrect_num:
            current += 1
        else:
            current = last + 1
            last = current
            sum = 0
            contiguous_set = []


### Part 1 ###
numbers = parse_input_file()
first_incorrect_num = find_first_incorrect_num(numbers, PREAMBLE_LENGTH)
print(first_incorrect_num)

### Part 2 ###
print(find_vuln(numbers, first_incorrect_num))