scores = []
for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    scores.append(score)

avr_score = sum(scores) // 5
print(avr_score)
