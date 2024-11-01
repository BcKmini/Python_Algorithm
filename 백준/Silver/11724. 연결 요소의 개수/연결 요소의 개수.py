import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

# 인접 리스트로 그래프
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# 간선 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 함수 
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

connected_components = 0
for i in range(1, N + 1):
    if not visited[i]:  
        dfs(i)
        connected_components += 1

# 결과 출력
print(connected_components)
