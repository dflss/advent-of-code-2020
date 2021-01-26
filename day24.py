import copy


def parse(s):
    row = 3
    col = 3
    while s:
        if s[0] == "w":
            # same row, col-1
            s = s[1:]
            col -= 1
        elif s[0] == "e":
            # same row, col+1
            s = s[1:]
            col += 1
        elif s[0:2] == "se":
            # even row: same col, row+1, odd row: both+1
            s = s[2:]
            if row % 2 == 0:
                row += 1
            else:
                col += 1
                row += 1
        elif s[0:2] == "sw":
            # even row: col-1, row+1, odd row: same col, row+1
            s = s[2:]
            if row % 2 == 0:
                row += 1
                col -= 1
            else:
                row += 1
        elif s[0:2] == "ne":
            # even row: same col, row-1, odd row: col+1, row-1
            s = s[2:]
            if row % 2 == 0:
                row -= 1
            else:
                col += 1
                row -= 1
        elif s[0:2] == "nw":
            # even row: both-1, odd row: same col, row-1
            s = s[2:]
            if row % 2 == 0:
                row -= 1
                col -= 1
            else:
                row -= 1
    return row, col


def part1():
    with open("day24_data.txt", "r") as file:
        input = file.readlines()
    black_tiles = []
    for line in input:
        tile = parse(line.strip())
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.append(tile)
    print(len(black_tiles))


def get_adjacent_tiles(tile):
    row, col = tile
    if row % 2 == 0:
        return [(row, col-1), (row, col+1), (row+1, col), (row+1, col-1), (row-1, col), (row-1, col-1)]
    else:
        return [(row, col-1), (row, col+1), (row+1, col+1), (row+1, col), (row-1, col+1), (row-1, col)]


def is_black_in_next_iter(tile, black_tiles):
    adjacent = get_adjacent_tiles(tile)
    count_black = 0
    for adj in adjacent:
        if adj in black_tiles:
            count_black += 1
    if tile not in black_tiles:
        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        return count_black == 2
    else:
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        return 0 < count_black <= 2


def part2():
    with open("day24_data.txt", "r") as file:
        input = file.readlines()
    black_tiles = []
    for line in input:
        tile = parse(line.strip())
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.append(tile)

    for i in range(100):
        next_black_tiles = set()
        for tile in black_tiles:
            if is_black_in_next_iter(tile, black_tiles):
                next_black_tiles.add(tile)
            for adj in get_adjacent_tiles(tile):
                if is_black_in_next_iter(adj, black_tiles):
                    next_black_tiles.add(adj)
        black_tiles = copy.deepcopy(next_black_tiles)
    print(len(black_tiles))


part1()
part2()