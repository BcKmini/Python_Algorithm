from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

def find_password(keylogs):
    result = []
    for keys in keylogs:
        left = deque()
        right = deque()
        for key in keys:
            if key == '<':
                if left:
                    right.appendleft(left.pop())
            elif key == '>':
                if right:
                    left.append(right.popleft())
            elif key == '-':
                if left:
                    left.pop()
            else:
                left.append(key)
        result.append(''.join(left) + ''.join(right))
    return result

test_cases = int(data[0])
keylogs = data[1:test_cases + 1]
answers = find_password(keylogs)
print('\n'.join(answers))
