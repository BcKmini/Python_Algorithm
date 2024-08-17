K, N, M = map(int, input().split())
total_cost = K * N

needed_money = total_cost - M
if needed_money > 0:
    print(needed_money)
else:
    print(0)
