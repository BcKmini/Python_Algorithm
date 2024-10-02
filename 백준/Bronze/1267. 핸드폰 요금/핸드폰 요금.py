n = int(input())
times = list(map(int, input().split()))

y_cost = 0
m_cost = 0

for time in times:
    y_cost += (time // 30 + 1) * 10
    m_cost += (time // 60 + 1) * 15

if y_cost < m_cost:
    print(f"Y {y_cost}")
elif y_cost > m_cost:
    print(f"M {m_cost}")
else:
    print(f"Y M {y_cost}")
