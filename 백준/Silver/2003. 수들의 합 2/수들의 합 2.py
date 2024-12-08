def solution(N, M, numbers):
    # 투 포인터 알고리즘
    count = 0
    start = 0
    current_sum = 0

    for end in range(N):
        current_sum += numbers[end]

        while current_sum >= M:
            if current_sum == M:
                count += 1
            current_sum -= numbers[start]
            start += 1
            
    return count

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

print(solution(N, M, numbers))