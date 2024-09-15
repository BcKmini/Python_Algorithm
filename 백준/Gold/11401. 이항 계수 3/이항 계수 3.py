MOD = 1000000007

def factorial(n):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    return fact

def mod_inverse(a, m):
    return pow(a, m - 2, m)

N, K = map(int, input().split())

if K == 0 or K == N:
    print(1)
else:
    fact = factorial(N)
    result = fact[N] * mod_inverse(fact[K], MOD) % MOD * mod_inverse(fact[N - K], MOD) % MOD
    print(result)
