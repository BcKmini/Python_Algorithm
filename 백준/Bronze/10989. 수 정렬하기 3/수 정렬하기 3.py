import sys
input = sys.stdin.readline
n = int(input())
count = [0] * 10001
for _ in range(n):
    count[int(input())] += 1
write = sys.stdout.write
for num in range(1, 10001):
    for _ in range(count[num]):
        write(str(num) + "\n")
