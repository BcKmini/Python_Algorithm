notes = list(map(int, input().split()))

if notes == sorted(notes):
    print("ascending")
elif notes == sorted(notes, reverse=True):
    print("descending")
else:
    print("mixed")
