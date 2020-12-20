import regex
import time


def parse_input_file():
    with open("day19_data.txt", "r") as file:
        return file.read().split('\n\n')


def substitute(rules, rule_index):
    subst = []
    subst.append('(')
    for char in rules[rule_index].split():
        if char.isdigit():
            subst.append(substitute(rules, int(char)))
        elif char == '|':
            subst.append(char)
        elif char.isalpha():
            return char
    subst.append(')')
    return ''.join(subst)


def part_1():
    input = parse_input_file()
    rules = {}
    words = input[1].splitlines()
    for line in input[0].splitlines():
        line_split = line.split(':')
        rules[int(line_split[0])] = line_split[1].strip().replace("\"", "")
    regex_0 = '^' + substitute(rules, 0) + '$'
    regex_final = regex.compile(regex_0)
    count = 0
    for word in words:
        if regex.match(regex_final, word):
            count += 1
    print(count)


def part_2():
    input = parse_input_file()
    rules = {}
    words = input[1].splitlines()
    for line in input[0].splitlines():
        line_split = line.split(':')
        rules[int(line_split[0])] = line_split[1].strip().replace("\"", "")
    regex_42 = substitute(rules, 42)
    regex_31 = substitute(rules, 31)
    regex_8 = f'({regex_42})+'
    name = 'group_11'
    regex_11 = f'(?P<{name}>{regex_42}(?P>{name})?{regex_31})'
    rules[8] = 'c'
    rules[11] = 'd'
    regex_0 = '^' + substitute(rules, 0) + '$'
    regex_0 = regex_0.replace('c', regex_8).replace('d', regex_11)
    regex_final = regex.compile(regex_0)
    count = 0
    for word in words:
        if regex.match(regex_final, word):
            count += 1
    print(count)

### Part 1 ###
start = time.perf_counter_ns()
part_1()
end = time.perf_counter_ns()
print(f"Part 1 took {(end - start)/1000000} ms")

### Part 1 ###
start = time.perf_counter_ns()
part_2()
end = time.perf_counter_ns()
print(f"Part 2 took {(end - start)/1000000} ms")
