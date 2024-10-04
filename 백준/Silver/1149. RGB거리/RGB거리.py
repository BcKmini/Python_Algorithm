N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])  # 빨강을 선택할 경우
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])  # 초록을 선택할 경우
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])  # 파랑을 선택할 경우

print(min(costs[N-1]))  # 마지막 집의 최소 비용 출력