def solve():
   
    T, W = map(int, input().split())
    plums = [0]  
    for _ in range(T):
        plums.append(int(input()))
    
    dp = [[[0] * 3 for _ in range(W + 1)] for _ in range(T + 1)]
    
   
    if plums[1] == 1:  # 첫 자두가 1번 나무에서 떨어질 경우
        dp[1][0][1] = 1
        dp[1][1][2] = 0
    else:  # 첫 자두가 2번 나무에서 떨어질 경우
        dp[1][0][1] = 0
        dp[1][1][2] = 1
    
    # dp 채우기
    for i in range(2, T + 1):  # 시간
        for j in range(W + 1):  # 이동 횟수
            for k in range(1, 3):  # 현재 위치
                if dp[i-1][j][k] == -1:  # 불가능한 경우 스킵
                    continue
                 
                if k == plums[i]:
                  
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + 1)
                        
                    if j < W:
                        next_pos = 3 - k 
                        dp[i][j+1][next_pos] = max(dp[i][j+1][next_pos], dp[i-1][j][k])
                 
                else:
                  
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
                   
                    if j < W:
                        next_pos = 3 - k  # 1->2 또는 2->1
                        dp[i][j+1][next_pos] = max(dp[i][j+1][next_pos], dp[i-1][j][k] + 1)   
   
    result = 0
    for j in range(W + 1):
        for k in range(1, 3):
            result = max(result, dp[T][j][k])
    
    return result

print(solve())