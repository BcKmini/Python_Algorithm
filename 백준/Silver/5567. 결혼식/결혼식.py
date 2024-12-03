from collections import defaultdict, deque

def count_wedding_guests(n, friendships):
    graph = defaultdict(list)
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set([1])  
    queue = deque([(1, 0)]) 
    
    while queue:
        student, distance = queue.popleft()
        
        if distance >= 2:
            continue
        
        for friend in graph[student]:
            if friend not in visited:
                visited.add(friend)
                queue.append((friend, distance + 1))
    
    return len(visited) - 1

n = int(input())  
m = int(input())  

friendships = []
for _ in range(m):
    a, b = map(int, input().split())
    friendships.append((a, b))

print(count_wedding_guests(n, friendships))