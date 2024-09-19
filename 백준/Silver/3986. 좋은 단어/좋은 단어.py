n = int(input())  # 단어의 수 입력
good_word_count = 0  # 좋은 단어의 수

for _ in range(n):
    word = input().strip()  # 단어 입력
    stack = []

    for char in word:
        if stack and stack[-1] == char:  # 스택의 마지막 문자와 현재 문자가 같다면 짝이 맞음
            stack.pop()  # 스택에서 제거
        else:
            stack.append(char)  # 그렇지 않으면 스택에 추가

    if not stack:  # 스택이 비어 있으면 좋은 단어
        good_word_count += 1

print(good_word_count)  # 좋은 단어의 수 출력
