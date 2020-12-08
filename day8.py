import copy
from dataclasses import dataclass


@dataclass
class Operation:
    op: str
    count: int


### Part 1 ###
with open("day8_data.txt", "r") as file:
    lines = file.readlines()
operations = []
for line in lines:
    line_split = line.split()
    operations.append(Operation(line_split[0], int(line_split[1])))
current = 0
acc_value = 0
visited = []
while True:
    if current in visited:
        break
    visited.append(current)
    if operations[current].op == 'nop':
        current += 1
    elif operations[current].op == 'acc':
        acc_value += operations[current].count
        current += 1
    elif operations[current].op == 'jmp':
        current = current + operations[current].count
print(acc_value)


### Part 2 ###

def is_infinite_loop(operations):
    current = 0
    visited = []
    while current < len(operations):
        if current in visited:
            return True
        visited.append(current)
        if operations[current].op == 'nop' or operations[current].op == 'acc':
            current += 1
        elif operations[current].op == 'jmp':
            current = current + operations[current].count
    return False

def get_acc_after_terminate(operations):
    current = 0
    acc_value = 0
    while current < len(operations):
        visited.append(current)
        if operations[current].op == 'nop':
            current += 1
        elif operations[current].op == 'acc':
            acc_value += operations[current].count
            current += 1
        elif operations[current].op == 'jmp':
            current = current + operations[current].count
    return acc_value

with open("day8_data.txt", "r") as file:
    lines = file.readlines()
operations = []
for line in lines:
    line_split = line.split()
    operations.append(Operation(line_split[0], int(line_split[1])))
current = 0
acc_value = 0
visited = []
loop = []
while True:
    if current in loop:
        break
    if current in visited:
        loop.append(current)
    else:
        visited.append(current)
    if operations[current].op == 'nop':
        current += 1
    elif operations[current].op == 'acc':
        acc_value += operations[current].count
        current += 1
    elif operations[current].op == 'jmp':
        current = current + operations[current].count

for index in loop:
    new_operations = copy.deepcopy(operations)
    if operations[index].op == 'jmp':
        new_operations[index].op = 'nop'
    elif operations[index].op == 'nop':
        new_operations[index].op = 'jmp'
    if not is_infinite_loop(new_operations):
        print(get_acc_after_terminate(new_operations))
        break
