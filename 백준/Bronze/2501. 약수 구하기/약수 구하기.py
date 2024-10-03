N, K = map(int, input().split())

divisors = []

for i in range(1, N+1):
    if N % i == 0:
        divisors.append(i)

if len(divisors) >= K:
    print(divisors[K-1])
else:
    print(0)
