import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_coprime_pairs(n):
    count = 0
    
    for a in range(1, int(math.sqrt(n)) + 1):
        
        if n % a == 0:
            b = n // a
            
            if gcd(a, b) == 1:
                count += 1
    
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_coprime_pairs(n))