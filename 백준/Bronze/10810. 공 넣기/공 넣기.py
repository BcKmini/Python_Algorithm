def baskets(N, M, operations):
    
    baskets = [0] * N
    for i, j, k in operations:
        for idx in range(i - 1, j):  
            baskets[idx] = k

    return baskets

N, M = map(int, input().split())
operations = [tuple(map(int, input().split())) for _ in range(M)]

result = baskets(N, M, operations)
print(" ".join(map(str, result)))
