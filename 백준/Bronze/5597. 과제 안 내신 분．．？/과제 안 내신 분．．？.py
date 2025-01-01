all_stu = set(range(1, 31))
submitted_stu = set(int(input()) for _ in range(28))

not_submit = sorted(all_stu - submitted_stu)

print(not_submit[0]) 
print(not_submit[1])  
