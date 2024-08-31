def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_prime_palindrome(N):
    while True:
        if is_prime(N) and is_palindrome(N):
            return N
        N += 1

N = int(input())
print(find_prime_palindrome(N))
