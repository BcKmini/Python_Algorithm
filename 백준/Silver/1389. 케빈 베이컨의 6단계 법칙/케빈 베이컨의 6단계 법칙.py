from collections import defaultdict, deque

def bfs(graph, start, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    

    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return sum(d for d in distances[1:] if d != float('inf'))

def find_number(n, m, friends):
    graph = defaultdict(list)
    for a, b in friends:
        graph[a].append(b)
        graph[b].append(a)
    
    kevin_bacon_numbers = [bfs(graph, i, n) for i in range(1, n + 1)]
    
    min_kevin_bacon_number = min(kevin_bacon_numbers)
    return kevin_bacon_numbers.index(min_kevin_bacon_number) + 1

n, m = map(int, input().split())
friends = [tuple(map(int, input().split())) for _ in range(m)]

print(find_number(n, m, friends))