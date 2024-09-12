def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

primes = [i for i in range(M, N + 1) if is_prime(i)]

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
