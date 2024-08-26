while True:
    n = int(input())
    if n == -1:
        break
    
    divisors = [i for i in range(1, n) if n % i == 0]
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
