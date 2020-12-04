### Part 1 ###

with open("day2_data.txt", "r") as file:
    lines = file.read().splitlines()
correct_count = 0
for line in lines:
    line_split = line.split()
    rule = line_split[0].split("-")
    rule_min = int(rule[0])
    rule_max = int(rule[1])
    rule_letter = line_split[1][0]
    password = line_split[2]
    letter_count = 0
    for letter in password:
        if letter == rule_letter:
            letter_count += 1
    if letter_count <= rule_max and letter_count >= rule_min:
        correct_count += 1
print(correct_count)

### Part 2 ###

with open("day2_data.txt", "r") as file:
    lines = file.read().splitlines()
correct_count = 0
for line in lines:
    line_split = line.split()
    rule = line_split[0].split("-")
    rule_min = int(rule[0])
    rule_max = int(rule[1])
    rule_letter = line_split[1][0]
    password = line_split[2]
    letter_count = 0
    if password[rule_min - 1] == rule_letter:
        letter_count += 1
    if password[rule_max - 1] == rule_letter:
        letter_count += 1
    if letter_count == 1:
        correct_count += 1
print(correct_count)

