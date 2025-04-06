import sys
data = sys.stdin.read().split()
n = int(data[0])
divs = list(map(int, data[1:]))
print(min(divs) * max(divs))