import time


def parse_input_file():
    with open("day17_data.txt", "r") as file:
        return file.readlines()


def part_1():
    to_add = {}
    def is_active(x, y, z, direction, layout, append_nonexisting):
        while True:
            x_ = x + direction[0]
            y_ = y + direction[1]
            z_ = z + direction[2]

            try:
                if layout[x_, y_, z_] == "#":
                    return 1
                elif layout[x_, y_, z_] == ".":
                    return 0
            except KeyError:
                if append_nonexisting:
                    to_add[x_, y_, z_] = '.'
                return 0

    def neighbors_active(x, y, z, layout, append_nonexisting):
        active = 0
        for x_ in range(-1, 2):
            for y_ in range(-1, 2):
                for z_ in range(-1, 2):
                    if x_ == y_ == z_ == 0:
                        continue
                    active += is_active(x_, y_, z_, (x, y, z,), layout, append_nonexisting)
        return active
    input = parse_input_file()
    layout = {}
    for i, row in enumerate(input):
        for j, seat in enumerate(row.strip()):
            layout[i, j, 0] = seat
    new_layout = {}
    for _ in range(6):
        for key, value in layout.items():
            active_neighbors = neighbors_active(*key, layout, append_nonexisting=True)
            if active_neighbors == 3:
                new_layout[key] = "#"
            elif value == "#" and active_neighbors == 2:
                new_layout[key] = "#"
            else:
                new_layout[key] = "."
        for key, value in to_add.items():
            active_neighbors = neighbors_active(*key, layout, append_nonexisting=False)
            if active_neighbors == 3:
                to_add[key] = "#"
            else:
                to_add[key] = '.'
        layout = {key: value for key, value in new_layout.items()}
        layout.update(to_add)
        to_add.clear()
    count = 0
    for v in layout.values():
        if v == "#":
            count += 1
    print(count)


def part_2():
    to_add = {}
    def is_active(x, y, z, w, direction, layout, append_nonexisting):
        while True:
            x_ = x + direction[0]
            y_ = y + direction[1]
            z_ = z + direction[2]
            w_ = w + direction[3]

            try:
                if layout[x_, y_, z_, w_] == "#":
                    return 1
                elif layout[x_, y_, z_, w_] == ".":
                    return 0
            except KeyError:
                if append_nonexisting:
                    to_add[x_, y_, z_, w_] = '.'
                return 0

    def neighbors_active(x, y, z, w, layout, append_nonexisting):
        active = 0
        for x_ in range(-1, 2):
            for y_ in range(-1, 2):
                for z_ in range(-1, 2):
                    for w_ in range(-1, 2):
                        if x_ == y_ == z_ == w_ == 0:
                            continue
                        active += is_active(x_, y_, z_, w_, (x, y, z, w), layout, append_nonexisting)
        return active
    input = parse_input_file()
    layout = {}
    for i, row in enumerate(input):
        for j, seat in enumerate(row.strip()):
            layout[i, j, 0, 0] = seat
    new_layout = {}
    for _ in range(6):
        for key, value in layout.items():
            active_neighbors = neighbors_active(*key, layout, append_nonexisting=True)
            if active_neighbors == 3:
                new_layout[key] = "#"
            elif value == "#" and active_neighbors == 2:
                new_layout[key] = "#"
            else:
                new_layout[key] = "."
        for key, value in to_add.items():
            active_neighbors = neighbors_active(*key, layout, append_nonexisting=False)
            if active_neighbors == 3:
                to_add[key] = "#"
            else:
                to_add[key] = '.'
        layout = {key: value for key, value in new_layout.items()}
        layout.update(to_add)
        to_add.clear()
    count = 0
    for v in layout.values():
        if v == "#":
            count += 1
    print(count)


### Part 1 ###
start = time.perf_counter_ns()
part_1()
end = time.perf_counter_ns()
print(f"Part 1 took {(end - start)/1000000} ms")

### Part 2 ###
start = time.perf_counter_ns()
part_2()
end = time.perf_counter_ns()
print(f"Part 2 took {(end - start)/1000000} ms")
