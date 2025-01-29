x, y, w, h = map(int, input().split())

distance = min(x, y, w - x, h - y)
print(distance)