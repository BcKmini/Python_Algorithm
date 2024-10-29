from itertools import combinations


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0

for i in range(1, N + 1):
    for subset in combinations(numbers, i):
        if sum(subset) == S:
            count += 1

print(count)
