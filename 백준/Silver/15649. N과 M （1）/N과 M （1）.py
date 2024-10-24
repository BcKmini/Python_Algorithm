from itertools import permutations

N, M = map(int, input().split())

perm = permutations(range(1, N+1), M)

for p in perm:
    print(' '.join(map(str, p)))
