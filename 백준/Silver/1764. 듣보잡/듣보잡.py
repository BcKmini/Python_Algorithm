N, M = map(int, input().split())

never_heard = set()
never_seen = set()

for _ in range(N):
    never_heard.add(input())

for _ in range(M):
    never_seen.add(input())

result = sorted(never_heard & never_seen)

print(len(result))
for name in result:
    print(name)
