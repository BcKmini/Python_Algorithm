def d(n):
    return n + sum(map(int, str(n)))

self_numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    generated_numbers.add(d(i))

self_numbers = self_numbers - generated_numbers

for number in sorted(self_numbers):
    print(number)
