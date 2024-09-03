n = int(input())
students = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    students.append((name, int(dd), int(mm), int(yyyy)))

students.sort(key=lambda x: (x[3], x[2], x[1]))

print(students[-1][0])
print(students[0][0])
