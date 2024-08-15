T = int(input())

for i in range(1, T + 1):
    A, B = map(int, input().split())
    result = A + B
    print(f"Case #{i}: {result}")
