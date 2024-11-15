def R(a, b, c):
    if b == 1:
        return a % c 
    
    half = R(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    else:
        return (half * a) % c
a, b, c = map(int, input().split())

print(R(a, b, c))
