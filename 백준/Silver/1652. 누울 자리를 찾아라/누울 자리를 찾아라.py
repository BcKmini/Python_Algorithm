N = int(input())
room = [input() for _ in range(N)]

def count_spaces(lines):
    count = 0
    for line in lines:
        space = 0
        for char in line:
            if char == '.':
                space += 1
            else:
                if space >= 2:
                    count += 1
                space = 0
        if space >= 2:
            count += 1
    return count

horizontal = count_spaces(room)
vertical = count_spaces(zip(*room))

print(horizontal, vertical)