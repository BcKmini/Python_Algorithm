import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

heap = []
result = []

for x in map(int, data[1:]):
    if x > 0:
        heapq.heappush(heap, -x)  # 최대 힙을 구현,  음수로 변환하여 삽입
    elif x == 0:
        if heap:
            result.append(-heapq.heappop(heap))  # 음수로 변환된 값을 다시 원래 값으로 출력
        else:
            result.append(0)

sys.stdout.write("\n".join(map(str, result)) + "\n")
