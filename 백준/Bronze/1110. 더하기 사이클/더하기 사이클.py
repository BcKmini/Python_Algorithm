n = int(input())

original = n
count = 0

while True:
    count += 1
    tens = n // 10
    ones = n % 10
    
    sum_ones = (tens + ones) % 10
    n = ones * 10 + sum_ones
   
    if n == original:
        break

print(count)
