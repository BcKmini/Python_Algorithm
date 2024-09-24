results = {0: 'D', 1: 'C', 2: 'B', 3: 'A', 4: 'E'}

for _ in range(3):
    yut = list(map(int, input().split()))
    print(results[sum(yut)])
