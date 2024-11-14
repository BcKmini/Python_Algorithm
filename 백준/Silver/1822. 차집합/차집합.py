n_a, n_b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))


difference = sorted(set_a - set_b)

if difference:
    print(len(difference))
    print(" ".join(map(str, difference)))
else:
    print(0)
