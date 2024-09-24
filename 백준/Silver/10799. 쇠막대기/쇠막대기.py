def count_iron_sticks(s):
    stack = []
    total_pieces = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:  # s[i] == ')'
            stack.pop()  # 일단 짝을 맞추기 위해 pop을 실행
            if s[i-1] == '(':  # 레이저인 경우
                total_pieces += len(stack)
            else:  # 쇠막대기의 끝인 경우
                total_pieces += 1
    
    return total_pieces

# 입력을 받고 결과 출력
s = input().strip()
print(count_iron_sticks(s))
