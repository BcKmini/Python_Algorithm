def tree_cutting(trees, m):
    # 이분 탐색의 범위를 설정
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        total = sum((tree - mid) for tree in trees if tree > mid)
        
        if total >= m:
            result = mid  # M 이상이면 더 높게 절단할 수 있는지 탐색
            low = mid + 1
        else:
            high = mid - 1
    
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(tree_cutting(trees, m))
