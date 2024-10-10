X = int(input())

# 이진수로 변환한 후 1의 개수를 세는 방법
count = bin(X).count('1')

print(count)
