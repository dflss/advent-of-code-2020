from collections import defaultdict


def parse_input_file():
    with open("day14_data.txt", "r") as file:
        return file.readlines()

def decimal_to_binary(num):
    return list(bin(num).replace("0b", "").zfill(36))

def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def part_1():
    input = parse_input_file()
    mask = ''
    memory = defaultdict(int)
    for line in input:
        line_content = [i.strip() for i in line.split('=')]
        if line_content[0] == 'mask':
            mask = line_content[1]
        else:
            address = int(line_content[0].split('[')[1].split(']')[0])
            value = decimal_to_binary(int(line_content[1]))

            for index, bit in enumerate(mask):
                if bit != 'X':
                    value[index] = bit
            value = binary_to_decimal(int(''.join(value)))
            memory[address] = value
    return sum(memory.values())

def part_2():
    input = parse_input_file()
    mask = ''
    memory = defaultdict(int)
    for line in input:
        line_content = [i.strip() for i in line.split('=')]
        if line_content[0] == 'mask':
            mask = line_content[1]
        else:
            address = decimal_to_binary(int(line_content[0].split('[')[1].split(']')[0]))
            addresses = [[]]
            value = int(line_content[1])
            for index, bit in enumerate(mask):
                if bit == 'X':
                    to_append = []
                    for addr in addresses:
                        new_addr = addr.copy()
                        addr.append('0')
                        new_addr.append('1')
                        to_append.append(new_addr)
                    addresses.extend(to_append)
                elif bit == '0':
                    for addr in addresses:
                        addr.append(address[index])
                else:
                    for addr in addresses:
                        addr.append(bit)
            for addr in addresses:
                memory[binary_to_decimal(int(''.join(addr)))] = value
    return sum(memory.values())

### Part 1 ###
print(part_1())

### Part 2 ###
print(part_2())