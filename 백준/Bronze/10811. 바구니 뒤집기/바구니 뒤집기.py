n, m = map(int, input().split())
baskets = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    baskets[i - 1:j] = reversed(baskets[i - 1:j])

print(*baskets)
