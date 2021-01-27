def find_loop_number(pubkey):
    value = 1
    count = 0
    while count < 10000000:
        count += 1
        prev = value
        value = (value * 7) % 20201227
        if value == pubkey:
            return count
        if prev == value:
            return None


def transform(loop, subject_number):
    value = 1
    count = 0
    for _ in range(0, loop):
        count += 1
        value = (value * subject_number) % 20201227
    return value


def part1():
    with open("day25_data.txt", "r") as file:
        input = file.readlines()
        pubkey_card, pubkey_door = int(input[0].strip()), int(input[1].strip())
        loop_card = find_loop_number(pubkey_card)
        loop_door = find_loop_number(pubkey_door)
        print(transform(loop_card, pubkey_door))
        print(transform(loop_door, pubkey_card))

part1()