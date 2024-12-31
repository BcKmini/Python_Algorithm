words = [input().strip() for _ in range(5)]

result = ""

for i in range(15):
    for word in words:
        if i < len(word): 
            result += word[i]

print(result)