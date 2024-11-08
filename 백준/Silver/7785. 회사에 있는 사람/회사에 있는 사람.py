n = int(input())
log = {}

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        log[name] = True  # 입장 시 기록
    elif action == "leave":
        if name in log:
            del log[name]  # 퇴장 시 제거

for name in sorted(log.keys(), reverse=True):
    print(name)