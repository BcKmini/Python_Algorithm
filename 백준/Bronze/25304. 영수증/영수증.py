X = int(input())

N = int(input())

calculated_total = 0
for _ in range(N):
    a, b = map(int, input().split())
    calculated_total += a * b

if calculated_total == X:
    print("Yes")
else:
    print("No")
