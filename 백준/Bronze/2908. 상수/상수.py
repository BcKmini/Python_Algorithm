a, b = input().split()

reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

print(max(reversed_a, reversed_b))