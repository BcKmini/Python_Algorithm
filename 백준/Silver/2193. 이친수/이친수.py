n = int(input())

# DP 테이블 초기화
dp = [0] * (n + 1)

# 초기값 설정
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 1

# DP 점화식을 이용해 계산
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# N자리 이친수 개수 출력
print(dp[n])
