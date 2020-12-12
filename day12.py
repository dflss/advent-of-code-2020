def parse_input_file():
    with open("day12_data.txt", "r") as file:
        return file.readlines()


### Part 1 ###
instructions = parse_input_file()
dirs_clockwise = ['E', 'S', 'W', 'N']
current_direction = 0
current_pos_x = 0
current_pos_y = 0
for instr in instructions:
    instr_strip = instr.strip()
    dir_ = instr_strip[0]
    count = int(instr_strip[1:])
    if dir_ == 'F':
        dir_ = dirs_clockwise[current_direction]
    if dir_ == 'E':
        current_pos_x += count
    elif dir_ == 'W':
        current_pos_x -= count
    elif dir_ == 'N':
        current_pos_y += count
    elif dir_ == 'S':
        current_pos_y -= count
    elif dir_ == 'R':
        current_direction = int((current_direction + (count/90)) % len(dirs_clockwise))
    elif dir_ == 'L':
        current_direction = int((current_direction - (count/90)) % len(dirs_clockwise))

print(abs(current_pos_x) + abs(current_pos_y))


### Part 2 ###
instructions = parse_input_file()
dirs_indices = {'E': 0, 'S': 1, 'W': 2, 'N':3}
waypoint = [10, 0, 0, 1]
position = [0, 0, 0, 0]

for instr in instructions:
    instr_strip = instr.strip()
    dir_ = instr_strip[0]
    count = int(instr_strip[1:])
    if dir_ == 'F':
        for i in range(len(waypoint)):
            position[i] += count * waypoint[i]
    elif dir_ == 'R':
        new_waypoint = []
        for i in range(len(waypoint)):
            new_waypoint.append(waypoint[(i - int(count/90)) % len(waypoint)])
        waypoint = new_waypoint
    elif dir_ == 'L':
        new_waypoint = []
        for i in range(len(waypoint)):
            new_waypoint.append(waypoint[(i + int(count/90)) % len(waypoint)])
        waypoint = new_waypoint
    else:
        waypoint[dirs_indices[dir_]] += count

current_pos_x = position[dirs_indices['E']] - position[dirs_indices['W']]
current_pos_y = position[dirs_indices['N']] - position[dirs_indices['S']]
print(abs(current_pos_x) + abs(current_pos_y))