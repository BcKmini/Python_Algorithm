X = int(input())

n = 1
while X > n:
    X -= n
    n += 1

if n % 2 == 0:
    print(f"{X}/{n+1-X}")
else:
    print(f"{n+1-X}/{X}")
