import copy


def parse_input_file():
    with open("day11_data.txt", "r") as file:
        return [[n for n in line.strip()] for line in file]


def gen_adjacent(matrix_2d, row, col):
    row_num = len(matrix_2d)
    col_num = len(matrix_2d[0])
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            if 0 <= row + r < row_num and 0 <= col + c < col_num:
                yield (row + r, col + c)


def is_seat(matrix_2d, row_num, col_num, current_row, current_col):
    return 0 <= current_row < row_num and 0 <= current_col < col_num and \
           (matrix_2d[current_row][current_col] in ['L', '#'])


def gen_first_seat_all_dir(matrix_2d, row, col):
    row_num = len(matrix_2d)
    col_num = len(matrix_2d[0])
    current_row = row
    current_col = col
    while current_row > 0:
        current_row -= 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_row < row_num:
        current_row += 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col > 0:
        current_col -= 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col < col_num:
        current_col += 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col > 0 and current_row > 0:
        current_col -= 1
        current_row -= 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col > 0 and current_row < row_num:
        current_col -= 1
        current_row += 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col < col_num and current_row > 0:
        current_col += 1
        current_row -= 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break
    current_row = row
    current_col = col
    while current_col < col_num and current_row < row_num:
        current_col += 1
        current_row += 1
        if is_seat(matrix_2d, row_num, col_num, current_row, current_col):
            yield (current_row, current_col)
            break

def is_adjacent_occupied(data, row, col):
    for adj in gen_adjacent(data, row, col):
        if data[adj[0]][adj[1]] == '#':
            return True
    return False


def is_first_seat_all_dir_occupied(data, row, col):
    for adj in gen_first_seat_all_dir(data, row, col):
        if data[adj[0]][adj[1]] == '#':
            return True
    return False


def is_four_or_more_adjacent_occupied(data, row, col):
    occupied_count = 0
    for adj in gen_adjacent(data, row, col):
        if data[adj[0]][adj[1]] == '#':
            occupied_count += 1
    return occupied_count >= 4


def is_five_or_more_first_seat_all_dir_occupied(data, row, col):
    occupied_count = 0
    for adj in gen_first_seat_all_dir(data, row, col):
        if data[adj[0]][adj[1]] == '#':
            occupied_count += 1
    return occupied_count >= 5


def apply_rule_1(data):
    data_copy = copy.deepcopy(data)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'L' and not is_adjacent_occupied(data, row, col):
                data_copy[row][col] = '#'
    return data_copy


def apply_rule_2(data):
    data_copy = copy.deepcopy(data)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '#' and is_four_or_more_adjacent_occupied(data, row, col):
                data_copy[row][col] = 'L'
    return data_copy


def apply_new_rule_1(data):
    data_copy = copy.deepcopy(data)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'L' and not is_first_seat_all_dir_occupied(data, row, col):
                data_copy[row][col] = '#'
    return data_copy


def apply_new_rule_2(data):
    data_copy = copy.deepcopy(data)
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '#' and is_five_or_more_first_seat_all_dir_occupied(data, row, col):
                data_copy[row][col] = 'L'
    return data_copy


data = parse_input_file()
while True:
    new_data = apply_rule_1(data)
    if data == new_data:
        break
    data = apply_rule_2(new_data)
    if data == new_data:
        break
occupied_count = 0
for row in data:
    for elem in row:
        if elem == '#':
            occupied_count += 1
print(occupied_count)


data = parse_input_file()
while True:
    new_data = apply_new_rule_1(data)
    if data == new_data:
        break
    data = apply_new_rule_2(new_data)
    if data == new_data:
        break
occupied_count = 0
for row in data:
    for elem in row:
        if elem == '#':
            occupied_count += 1
print(occupied_count)
