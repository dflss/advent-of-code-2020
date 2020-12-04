with open("day3_data.txt", "r") as file:
    lines = file.read().splitlines()

def slope(right, down):
    pattern_length = len(lines[0])
    offset = 0
    tree_count = 0
    for i in range(down, len(lines), down):
        offset += right
        offset = offset % pattern_length
        if lines[i][offset] == '#':
            tree_count += 1
    return tree_count


### Part 1 ###
print(slope(3,1))

### Part 2 ###
print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))