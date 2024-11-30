def solve_path_finding(N, graph):

    for k in range(N):
        for i in range(N):
            for j in range(N):
              
                graph[i][j] |= (graph[i][k] and graph[k][j])
    
    return graph

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = solve_path_finding(N, graph)


for row in result:
    print(' '.join(map(str, row)))