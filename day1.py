def find2020_2(numbers):
    for i, number in enumerate(numbers):
        for j, number2 in enumerate(numbers, i):
            if int(number) + int(number2) == 2020:
                return (number, number2, int(number)*int(number2))

def find2020_3(numbers):
    for i, number in enumerate(numbers):
        for j, number2 in enumerate(numbers, i):
            for k, number3 in enumerate(numbers, j):
                if int(number) + int(number2) + int(number3) == 2020:
                    return (number, number2, number3, int(number)*int(number2)*int(number3))

with open("day1_data.txt", "r") as file:
    numbers = file.read().splitlines()
print(find2020_2(numbers))
print(find2020_3(numbers))
