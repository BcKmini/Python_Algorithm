def count_seconds(N):
    seconds = 0
    current = 1  

    while N > 0:
        if N < current:
            current = 1  
        N -= current  
        seconds += 1 
        current += 1 

    return seconds

N = int(input())
print(count_seconds(N))
