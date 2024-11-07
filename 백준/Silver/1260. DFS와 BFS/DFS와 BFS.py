from collections import deque, defaultdict

def dfs(graph, start, visited):
    visited[start] = True
    result = [start]
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            result.extend(dfs(graph, neighbor, visited))
    return result

def bfs(graph, start):
    visited = {node: False for node in graph}
    visited[start] = True
    queue = deque([start])
    result = [start]
    
    while queue:
        node = queue.popleft()
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                result.append(neighbor)
    return result

n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS와 BFS 결과 
visited = {node: False for node in graph}
print(" ".join(map(str, dfs(graph, v, visited))))
print(" ".join(map(str, bfs(graph, v))))
