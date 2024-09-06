heights = [int(input()) for _ in range(9)]
total = sum(heights)

for i in range(9):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            heights.remove(heights[i])
            heights.remove(heights[j - 1])
            break
    if len(heights) == 7:
        break

heights.sort()
for height in heights:
    print(height)
