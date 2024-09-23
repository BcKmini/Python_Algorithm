cards = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    cards[a-1:b] = cards[a-1:b][::-1]

print(' '.join(map(str, cards)))
