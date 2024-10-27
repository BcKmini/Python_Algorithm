import sys
input = sys.stdin.read

def find_president():
    data = input().splitlines()
    n = int(data[0])  # 회원 수
    INF = float('inf')

    # 인접 행렬 초기화
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        distance[i][i] = 0

    
    for line in data[1:]:
        a, b = map(int, line.split())
        if a == -1 and b == -1:
            break
        distance[a][b] = 1
        distance[b][a] = 1

    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

   
    scores = [max(distance[i][1:]) for i in range(1, n + 1)]
    min_score = min(scores)

    
    candidates = [i + 1 for i in range(n) if scores[i] == min_score]

    # 결과 출력
    print(min_score, len(candidates))
    print(*candidates)

find_president()
