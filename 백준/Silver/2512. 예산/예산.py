def get_budget_sum(budgets, cap):
    """상한액 cap을 기준으로 배정된 예산의 총합을 계산"""
    total = 0
    for budget in budgets:
        total += min(budget, cap)
    return total

# 입력 받기
n = int(input())  
budgets = list(map(int, input().split()))  # 각 지방의 예산 요청
total_budget = int(input())  # 국가의 총 예산

# 이분 탐색을 위한 변수 설정
left, right = 0, max(budgets)  # 상한액 범위
result = 0

# 이분 탐색 수행
while left <= right:
    mid = (left + right) // 2
    current_sum = get_budget_sum(budgets, mid)
    
    if current_sum <= total_budget:  # 배정된 예산이 총 예산 이하인 경우
        result = mid  # 현재 상한액을 저장하고, 더 큰 상한액을 시도
        left = mid + 1
    else:  # 배정된 예산이 총 예산을 초과한 경우
        right = mid - 1

# 결과 출력
print(result)
