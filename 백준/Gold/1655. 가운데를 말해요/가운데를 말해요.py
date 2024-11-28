import sys
import heapq

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:]))

max_heap = []  
min_heap = []  

result = []

for number in numbers:
    heapq.heappush(max_heap, -number)

    if min_heap and (-max_heap[0] > min_heap[0]):
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    result.append(-max_heap[0])

print('\n'.join(map(str, result)))
