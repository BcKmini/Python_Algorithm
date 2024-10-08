t = int(input())

for _ in range(t):
    n = int(input())
    phone_numbers = [input().strip() for _ in range(n)]
    
    # 전화번호 목록을 사전순으로 정렬
    phone_numbers.sort()
    
    # 인접한 번호들끼리만 비교
    is_consistent = True
    for i in range(n - 1):
        # 앞 번호가 뒷 번호의 접두어인지 확인
        if phone_numbers[i] == phone_numbers[i+1][:len(phone_numbers[i])]:
            is_consistent = False
            break
    
    # 결과 출력
    if is_consistent:
        print("YES")
    else:
        print("NO")
