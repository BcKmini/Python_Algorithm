def egg_game(index, eggs, broken_count):
    global max_broken
    if index == len(eggs):
        max_broken = max(max_broken, broken_count)
        return
    
    # 현재 계란이 이미 깨져있다면 다음 계란으로 넘어감
    if eggs[index][0] <= 0:
        egg_game(index + 1, eggs, broken_count)
        return
    
    
    hit = False
    for i in range(len(eggs)):
        if i != index and eggs[i][0] > 0:
            hit = True
            # 현재 계란과 i번째 계란 충돌
            eggs[index][0] -= eggs[i][1]
            eggs[i][0] -= eggs[index][1]
            
            # 깨진 계란 수 계산
            new_broken_count = broken_count
            if eggs[index][0] <= 0:
                new_broken_count += 1
            if eggs[i][0] <= 0:
                new_broken_count += 1
            
            # 재귀 호출
            egg_game(index + 1, eggs, new_broken_count)
            
            # 상태 복원
            eggs[index][0] += eggs[i][1]
            eggs[i][0] += eggs[index][1]
    
    if not hit:
        egg_game(index + 1, eggs, broken_count)

# 입력 받기
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

# 결과 초기화 및 함수 호출
max_broken = 0
egg_game(0, eggs, 0)
print(max_broken)
