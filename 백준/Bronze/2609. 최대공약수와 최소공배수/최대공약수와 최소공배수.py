import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)
lcm = a * b // gcd

print(gcd)
print(lcm)