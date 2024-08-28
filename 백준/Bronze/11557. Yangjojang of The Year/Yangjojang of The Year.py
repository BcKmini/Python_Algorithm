T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 학교의 수
    max_liquor = 0
    max_school = ""
    
    for _ in range(N):
        school, liquor = input().split()
        liquor = int(liquor)
        
        if liquor > max_liquor:
            max_liquor = liquor
            max_school = school
    
    print(max_school)