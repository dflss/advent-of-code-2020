from collections import deque
from itertools import islice


def parse_input_file():
    with open("day22_data.txt", "r") as file:
        return file.read().split('\n\n')


def part_1():
    input = parse_input_file()
    deck1 = deque([int(i) for i in input[0].splitlines()[1:]])
    deck2 = deque([int(i) for i in input[1].splitlines()[1:]])
    while not (len(deck1) == 0 or len(deck2) == 0):
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    score = 0
    winning_deck = deck1 if len(deck1) > 0 else deck2
    for i, card in enumerate(reversed(winning_deck)):
        score += (i + 1) * card
    print(score)


def play(deck1, deck2, first_round):
    if max(deck1) > max(deck2) and not first_round:
        return 1, deck1
    states = set()
    while not (len(deck1) == 0 or len(deck2) == 0):
        if (state := (tuple(deck1), tuple(deck2))) in states:
            return 1, deck1
        states.add(state)
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            subdeck1 = deque(islice(deck1, 0, card1))
            subdeck2 = deque(islice(deck2, 0, card2))
            winner, _ = play(subdeck1, subdeck2, False)
            if winner == 1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
    return (1, deck1) if len(deck1) > 0 else (2, deck2)


def part_2():
    input = parse_input_file()
    deck1 = deque([int(i) for i in input[0].splitlines()[1:]])
    deck2 = deque([int(i) for i in input[1].splitlines()[1:]])
    winner, winning_deck = play(deck1, deck2, True)
    score = 0
    for i, card in enumerate(reversed(winning_deck)):
        score += (i + 1) * card
    print(score)


part_1()
part_2()