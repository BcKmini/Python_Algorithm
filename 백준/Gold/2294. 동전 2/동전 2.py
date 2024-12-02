import sys

def min_coins(n, k, coins):
    dp = [k+1] * (k+1)
    dp[0] = 0 
    
    for i in range(1, k+1):
       
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    
    return dp[k] if dp[k] != k+1 else -1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(min_coins(n, k, coins))