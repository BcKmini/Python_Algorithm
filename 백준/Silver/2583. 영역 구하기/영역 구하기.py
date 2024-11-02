import sys
from collections import deque

input = sys.stdin.readline

# 모눈종이의 세로 크기 M, 가로 크기 N, 직사각형의 개수 K
M, N, K = map(int, input().split())

# 모눈종이를 표현하는 2차원 배열
grid = [[0] * N for _ in range(M)]

# 직사각형
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

# 상하좌우 방향을 나타내는 이동 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 함수 정의
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = 1  # 방문 처리
    area_size = 0
    
    while queue:
        x, y = queue.popleft()
        area_size += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 방문 처리
                queue.append((nx, ny))
    
    return area_size

# 각 영역의 넓이를 저장할 리스트
areas = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            area_size = bfs(i, j)
            areas.append(area_size)

print(len(areas)) 
print(" ".join(map(str, sorted(areas)))) 
