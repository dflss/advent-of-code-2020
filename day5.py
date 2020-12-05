def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def get_highest_seat_id():
    with open("day5_data.txt", "r") as file:
        lines = file.readlines()
    binary_row = []
    binary_col = []
    for line in lines:
        binary_row.append(int(line.replace("F", "0").replace("B", "1")[:7]))
        binary_col.append(line[7:].strip())
    index = binary_row.index(max(binary_row))
    row = binary_to_decimal(binary_row[index])
    col = binary_to_decimal(int(binary_col[index].replace("L", "0").replace("R", "1")))
    return row * 8 + col

def get_seat_id(value):
    row = binary_to_decimal(int(value.replace("F", "0").replace("B", "1")[:7]))
    col = binary_to_decimal(int(value.replace("L", "0").replace("R", "1")[7:]))
    return row * 8 + col

def get_missing_seat_id():
    seats = [0] * 1024
    with open("day5_data.txt", "r") as file:
        lines = file.readlines()
    ids = list(get_seat_id(i.strip()) for i in lines)
    for id in ids:
        seats[id] = 1
    for id, occupied in enumerate(seats):
        if not occupied:
            if seats[id - 1] == 1 and seats[id + 1] == 1:
                return id


### Part 1 ###
print(get_highest_seat_id())

### Part 2 ###
print(get_missing_seat_id())
