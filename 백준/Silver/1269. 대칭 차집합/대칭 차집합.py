import sys
input = sys.stdin.read
data = input().splitlines()

a_size, b_size = map(int, data[0].split())

set_a = set(map(int, data[1].split()))
set_b = set(map(int, data[2].split()))

sym_diff = (set_a - set_b) | (set_b - set_a)
print(len(sym_diff))
