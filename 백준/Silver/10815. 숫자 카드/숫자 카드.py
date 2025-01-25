import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
sang_card = set(map(int, data[1:N+1]))

M = int(data[N+1])
check_nums = list(map(int, data[N+2:]))

result = []
for num in check_nums:
    result.append(1 if num in sang_card else 0)

print(' '.join(map(str, result)))