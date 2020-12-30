NO_MOVES_P1 = 100
NO_MOVES_P2 = 10000000


def wrapping_slice(lst, *args):
    return [lst[i%len(lst)] for i in range(*args)]


def del_wrapping_slice(lst, *args):
    indices = [i%len(lst) for i in range(*args)]
    return [i for j, i in enumerate(lst) if j not in indices]


def find_dest_cup_ix(new_cups, current_cup):
    dest_cup = current_cup - 1
    while True:
        if dest_cup in new_cups:
            return new_cups.index(dest_cup)
        dest_cup = (dest_cup - 1) if dest_cup >= min(new_cups) else max(new_cups)


def part1():
    with open("day23_data.txt", "r") as file:
        cups = [int(i) for i in list(file.read())]
    current_cup_ix = 0

    for i in range(NO_MOVES_P1):
        current_cup = cups[current_cup_ix]
        cups_to_move = wrapping_slice(cups, current_cup_ix+1, current_cup_ix+4)
        new_cups = del_wrapping_slice(cups, current_cup_ix + 1, current_cup_ix + 4)
        dest_cup_ix = find_dest_cup_ix(new_cups, current_cup)
        new_cups[dest_cup_ix+1:dest_cup_ix+1] = cups_to_move
        cups = new_cups
        current_cup_ix = (new_cups.index(current_cup) + 1) % len(cups)

    index_1 = cups.index(1)
    final = cups[index_1 + 1 :] + cups[:index_1]

    print(f"Part 1: {''.join(str(x) for x in final)}")


def move(current_cup, succ):
    p0 = succ[current_cup]
    p1 = succ[p0]
    p2 = succ[p1]
    next_cup = succ[p2]
    dest_cup = current_cup - 1

    while True:
        if dest_cup < 1:
            dest_cup = max(succ)
        if dest_cup not in (p0, p1, p2):
            break
        dest_cup = dest_cup - 1

    succ[current_cup] = next_cup
    succ[p2] = succ[dest_cup]
    succ[dest_cup] = p0
    return next_cup


def part2():
    with open("day23_data.txt", "r") as file:
        cups = [int(i) for i in list(file.read())]

    cups.extend([i for i in range(max(cups) + 1, 1000000 + 1)])
    current_cup = cups[0]
    successors = [0] * (len(cups) + 1)

    for i in range(len(cups) - 1):
        successors[cups[i]] = cups[i + 1]
    successors[cups[-1]] = current_cup

    for _ in range(NO_MOVES_P2):
        current_cup = move(current_cup, successors)

    print(f"Part 2: {successors[1] * successors[successors[1]]}")


part1()
part2()