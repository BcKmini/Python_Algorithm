from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N + 1))
result = []

# 큐를 순회하면서 K번째 사람 제거
while people:
    # K번째 사람을 제거하기 위해 앞에서 K-1명까지 뒤로 보냄
    people.rotate(-(K-1))
    # K번째 사람 제거 및 결과에 추가
    result.append(people.popleft())

print("<" + ", ".join(map(str, result)) + ">")