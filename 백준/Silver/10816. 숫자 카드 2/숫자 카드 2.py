from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

card_count = Counter(cards)

result = [card_count[query] for query in queries]
print(' '.join(map(str, result)))
