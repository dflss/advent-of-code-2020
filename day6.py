def get_anyone_question_number():
    with open("day6_data.txt", "r") as file:
        input = file.read()
    groups = input.split("\n\n")
    question_number = 0
    for group in groups:
        unique_letters = set()
        for letter in group.replace("\n", ""):
            unique_letters.add(letter)
        question_number += len(unique_letters)
    return question_number


def get_everyone_question_number():
    with open("day6_data.txt", "r") as file:
        input = file.read()
    groups = input.split("\n\n")
    question_number = 0
    for group in groups:
        individual_responses = group.split("\n")
        response_setlist = []
        for resp in individual_responses:
            response_setlist.append(set(resp))
        resp_everyone = set.intersection(*response_setlist)
        question_number += len(resp_everyone)
    return question_number

### Part 1 ###
print(get_anyone_question_number())

### Part 2 ###
print(get_everyone_question_number())