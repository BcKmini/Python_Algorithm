n = int(input())  
sequence = [int(input()) for _ in range(n)]  

stack = []
result = []
current = 1  # 현재 스택에 넣을 숫자
possible = True  # 수열을 만들 수 있는지 여부

for number in sequence:
    # 현재 숫자까지 스택에 push
    while current <= number:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택의 마지막 값이 수열의 숫자와 일치하면 pop
    if stack[-1] == number:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")
