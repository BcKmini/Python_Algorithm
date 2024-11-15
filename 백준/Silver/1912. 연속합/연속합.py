def max_subarray_sum(n, arr):
    
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, n):
        
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


n = int(input())
arr = list(map(int, input().split()))


print(max_subarray_sum(n, arr))
