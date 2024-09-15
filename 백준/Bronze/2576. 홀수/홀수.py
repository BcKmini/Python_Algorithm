numbers = [int(input()) for _ in range(7)]

odds = [num for num in numbers if num % 2 != 0]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
