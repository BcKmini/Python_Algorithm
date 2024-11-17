import sys
input = sys.stdin.readline

N = int(input())  
heights = list(map(int, input().split()))  

stack = []  
result = [0] * N  

for i in range(N):
    # 현재 탑보다 낮은 탑은 신호를 수신하지 못함
    while stack and stack[-1][0] < heights[i]:
        stack.pop()
    
    # 스택이 비어있지 않다면 가장 가까운 높은 탑의 인덱스 저장
    if stack:
        result[i] = stack[-1][1] + 1  # 

    # 현재 탑을 스택에 추가
    stack.append((heights[i], i))


print(" ".join(map(str, result)))
