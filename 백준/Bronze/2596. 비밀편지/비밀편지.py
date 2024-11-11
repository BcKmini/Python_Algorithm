codes = {
    'A': '000000',
    'B': '001111',
    'C': '010011',
    'D': '011100',
    'E': '100110',
    'F': '101001',
    'G': '110101',
    'H': '111010'
}


n = int(input())
message = input()


result = []

# 6비트씩 분할, 해석
for i in range(n):
    segment = message[i*6:(i+1)*6]
    found = False
    
    # 각 문자 코드와 비교하여 틀린 비트가 1개 이하인지 확인
    for char, code in codes.items():
        # 틀린 비트 수 계산
        diff_count = sum(1 for x, y in zip(segment, code) if x != y)
        
        if diff_count <= 1:
            result.append(char)
            found = True
            break
    
    # 일치하는 문자가 없으면 위치 출력, 종료
    if not found:
        print(i + 1)
        break
else:
    
    print("".join(result))
