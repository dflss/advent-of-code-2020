import math


def parse_input_file():
    with open("day20_data.txt", "r") as file:
        input = file.read()
    return input.split("\n\n")


def count_aligns(tile, tiles):
    count = 0
    for t in tiles:
        if not tile == t:
            for edge1 in tile:
                for edge2 in t:
                    if edge1 == edge2:
                        count += 1
    return count/2


def part_1():
    tiles = {}
    input = parse_input_file()
    for tile in input:
        lines = tile.splitlines()
        tile_num = int(lines[0].split()[1].strip(':'))
        up = lines[1]
        down = lines[-1]
        right_arr = []
        left_arr = []
        for line in lines[1:]:
            left_arr.append(line[0])
            right_arr.append(line[-1])
        right = ''.join(right_arr)
        left = ''.join(left_arr)
        tiles[tile_num] = [up,
                           up[::-1],
                           right,
                           right[::-1],
                           down,
                           down[::-1],
                           left,
                           left[::-1]
                           ]
    corners = []
    for key, tile in tiles.items():
        if count_aligns(tile, tiles.values()) == 2:
            corners.append(key)
    print(math.prod(corners))


def part_2():
    input = parse_input_file()


part_1()
part_2()