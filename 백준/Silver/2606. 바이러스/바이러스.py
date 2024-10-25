def dfs(graph, visited, node):
    visited[node] = True
    count = 1  
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)
    
    return count

n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 연결 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
infected_count = dfs(graph, visited, 1) - 1  # 1번 컴퓨터는 제외

print(infected_count)
