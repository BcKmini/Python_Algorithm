def calc_parentheses_value(s):
    stack = []
    result = 0
    temp = 1
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            temp *= 2
        elif s[i] == '[':
            stack.append('[')
            temp *= 3
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if s[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif s[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if s[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
    
    if stack:
        return 0
    return result

s = input().strip()
print(calc_parentheses_value(s))
