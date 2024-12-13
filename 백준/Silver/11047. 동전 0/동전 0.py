def coin_count(n, k, coins):
    count = 0
    for coin in reversed(coins):
        if k == 0:
            break
        count += k // coin
        k %= coin
    return count
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(coin_count(n, k, coins))
