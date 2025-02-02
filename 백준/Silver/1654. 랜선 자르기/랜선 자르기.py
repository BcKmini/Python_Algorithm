import sys

def count_cables(lines, length):
    return sum(line // length for line in lines)

def max_cable(K, N, lines):
    low, high = 1, max(lines)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2  
        count = count_cables(lines, mid) 
        
        if count >= N: 
            result = mid
            low = mid + 1
        else:  
            high = mid - 1
            
    return result

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

print(max_cable(K, N, lines))