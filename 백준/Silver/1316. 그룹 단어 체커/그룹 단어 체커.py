
n = int(input())
words = [input().strip() for _ in range(n)]

group_word_count = 0

for word in words:
    is_group_word = True
    seen = set()  
    previous_char = ''  # 이전 문자 초기화

    for char in word:
        # 이전 문자와 현재 문자가 다르고, 현재 문자가 이미 등장했다면 그룹 단어가 아님
        if char != previous_char and char in seen:
            is_group_word = False
            break
        seen.add(char)
        previous_char = char  

    
    if is_group_word:
        group_word_count += 1

print(group_word_count)
