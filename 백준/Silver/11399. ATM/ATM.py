N = int(input())
times = list(map(int, input().split()))
times.sort()

result = 0
acc = 0
for t in times:
    acc += t
    result += acc
print(result)