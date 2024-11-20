import heapq
import sys

def minimum_merge_cost(test_cases):
    results = []
    for case in test_cases:
        k, file_sizes = case
        
        heapq.heapify(file_sizes)
        
        total_cost = 0
        while len(file_sizes) > 1:
         
            smallest = heapq.heappop(file_sizes)
            second_smallest = heapq.heappop(file_sizes)
            cost = smallest + second_smallest
            total_cost += cost
            heapq.heappush(file_sizes, cost)
        
        results.append(total_cost)
    return results

def main():
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0]) 
    test_cases = []
    index = 1
    
    for _ in range(T):
        K = int(data[index])
        index += 1
        file_sizes = list(map(int, data[index:index + K]))
        index += K
        test_cases.append((K, file_sizes))
    
    results = minimum_merge_cost(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
