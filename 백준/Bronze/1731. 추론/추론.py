n = int(input())
sequence = [int(input()) for _ in range(n)]


if sequence[1] - sequence[0] == sequence[2] - sequence[1]:  
    diff = sequence[1] - sequence[0]
    next_term = sequence[-1] + diff
else:  
    ratio = sequence[1] // sequence[0]
    next_term = sequence[-1] * ratio

print(next_term)
