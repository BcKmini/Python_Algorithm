import math

A, B, V = map(int, input().split())
days = math.ceil((V - B) / (A - B))
print(days)