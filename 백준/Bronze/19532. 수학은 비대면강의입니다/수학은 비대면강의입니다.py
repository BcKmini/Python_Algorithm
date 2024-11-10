
a, b, c, d, e, f = map(int, input().split())

deno = a * e - b * d
x = (c * e - b * f) // deno
y = (a * f - c * d) // deno


print(x, y)
