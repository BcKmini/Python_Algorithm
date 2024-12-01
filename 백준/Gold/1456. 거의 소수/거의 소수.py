import math

def count_almost_primes(A, B):
    max_prime = int(math.sqrt(B)) + 1
    is_prime = [True] * (max_prime + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(max_prime)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_prime + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, max_prime + 1) if is_prime[i]]

    count = 0
    for p in primes:
        power = p * p 
        while power <= B:
            if power >= A:
                count += 1
            if power > B // p:  
                break
            power *= p  
    return count

A, B = map(int, input().split())
print(count_almost_primes(A, B))
