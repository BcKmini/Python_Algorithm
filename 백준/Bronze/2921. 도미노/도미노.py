N = int(input())
total_sum = 0

for a in range(N + 1):
    for b in range(a, N + 1):
        total_sum += a + b

print(total_sum)