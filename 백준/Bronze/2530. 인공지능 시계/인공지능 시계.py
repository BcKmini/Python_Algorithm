A, B, C = map(int, input().split())
D = int(input())

total_seconds = A * 3600 + B * 60 + C

total_seconds += D

A = (total_seconds // 3600) % 24
B = (total_seconds % 3600) // 60
C = total_seconds % 60

print(A, B, C)
