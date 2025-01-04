from itertools import combinations

def blackjack(N, M, cards):
    card_combinations = combinations(cards, 3)
    max_sum = 0
    
    for comb in card_combinations:
        card_sum = sum(comb)
        if card_sum <= M:
            max_sum = max(max_sum, card_sum)
    
    return max_sum

N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack(N, M, cards))
