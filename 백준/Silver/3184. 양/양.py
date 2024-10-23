from collections import deque

# 방향 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 이용한 영역 탐색
def bfs(x, y):
    queue = deque([(x, y)])
    sheep, wolf = 0, 0

    if yard[x][y] == 'o':
        sheep += 1
    elif yard[x][y] == 'v':
        wolf += 1

    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and yard[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
                
                if yard[nx][ny] == 'o':
                    sheep += 1
                elif yard[nx][ny] == 'v':
                    wolf += 1

    
    return sheep, wolf


R, C = map(int, input().split())
yard = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

total_sheep, total_wolf = 0, 0

# 전체 마당을 순회/탐색
for i in range(R):
    for j in range(C):
        if not visited[i][j] and yard[i][j] != '#':
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)
