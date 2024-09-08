import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
idx = 1

for _ in range(T):
    k = int(data[idx])
    idx += 1
    min_heap, max_heap = [], []
    entry_finder = {}
    
    for _ in range(k):
        operation = data[idx]
        idx += 1
        cmd, num = operation.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_finder[num] = entry_finder.get(num, 0) + 1
        
        elif cmd == 'D':
            if num == 1:
                while max_heap and entry_finder[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] -= 1
            elif num == -1:
                while min_heap and entry_finder[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] -= 1
    
    while min_heap and entry_finder[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_finder[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(f"{-max_heap[0]} {min_heap[0]}")
