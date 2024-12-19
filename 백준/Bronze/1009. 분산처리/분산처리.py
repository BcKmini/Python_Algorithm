def last_com(t, cases):
    results = []
    for a, b in cases:
        base = a % 10

        if base == 0:
            results.append(10)  
        else:
            cycle = []
            value = base
            while value not in cycle:
                cycle.append(value)
                value = (value * base) % 10
            
            index = (b - 1) % len(cycle)
            results.append(cycle[index])
    return results

t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]

results = last_com(t, cases)
for result in results:
    print(result)
