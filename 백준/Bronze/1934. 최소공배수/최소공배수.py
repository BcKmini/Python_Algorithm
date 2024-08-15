import math

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    lcm = (A * B) // math.gcd(A, B)

    print(lcm)
