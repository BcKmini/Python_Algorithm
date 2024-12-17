def min_s_value(n, a, b):
    a.sort()
    b.sort(reverse=True)

    s = sum(a[i] * b[i] for i in range(n))
    return s

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(min_s_value(n, a, b))
