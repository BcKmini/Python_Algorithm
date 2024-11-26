from math import gcd

A, B = map(int, input().split())

numerator = B - A  # 분자
denominator = B    # 분모

g = gcd(numerator, denominator)
numerator //= g
denominator //= g

print(numerator, denominator)
