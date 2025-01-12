def base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while N > 0:
        remainder = N % B
        result.append(digits[remainder])
        N //= B
    return ''.join(result[::-1])

N, B = map(int, input().split())

print(base(N, B))
