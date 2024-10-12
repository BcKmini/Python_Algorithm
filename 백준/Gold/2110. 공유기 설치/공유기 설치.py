def can_install_routers(houses, distance, C):
    count = 1  # 첫 번째 집에 무조건 설치
    last_installed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
        if count >= C:
            return True
    return False

def max_min_distance(N, C, houses):
    houses.sort()  # 집의 좌표 정렬
    
    left = 1  # 가능한 최소 거리
    right = houses[-1] - houses[0]  # 가능한 최대 거리
    result = 0

    while left <= right:
        mid = (left + right) // 2  # 중간 거리
        
        if can_install_routers(houses, mid, C):
            result = mid  # 설치 가능하면 거리를 늘려본다
            left = mid + 1
        else:
            right = mid - 1

    return result

# 입력 처리
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# 결과 출력
print(max_min_distance(N, C, houses))
