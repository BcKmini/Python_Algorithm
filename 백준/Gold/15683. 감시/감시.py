import copy

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

CCTV_DIRECTIONS = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}

def monitor_area(board, x, y, directions):
    n, m = len(board), len(board[0])
    for direction in directions:
        dx, dy = DIRECTIONS[direction]
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
            if board[nx][ny] == 0:
                board[nx][ny] = '#'
            nx += dx
            ny += dy

def backtrack(cctvs, board, idx):
    global min_blind_spot

    if idx == len(cctvs):
        
        blind_spot = sum(row.count(0) for row in board)
        min_blind_spot = min(min_blind_spot, blind_spot)
        return

    x, y, cctv_type = cctvs[idx]
    for directions in CCTV_DIRECTIONS[cctv_type]:

        new_board = copy.deepcopy(board)
        monitor_area(new_board, x, y, directions)
       
        backtrack(cctvs, new_board, idx + 1)

n, m = map(int, input().split())
board = []
cctvs = []

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

min_blind_spot = float('inf')

backtrack(cctvs, board, 0)

print(min_blind_spot)
