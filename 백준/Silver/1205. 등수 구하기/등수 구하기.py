def solution():
    N, new_score, P = map(int, input().split())
    
    if N == 0:
        return 1
    
    ranking = list(map(int, input().split())) if N > 0 else []
    
    if len(ranking) == P and new_score <= ranking[-1]:
        return -1
    
    rank = 1
    for score in ranking:
        if new_score >= score:
            return rank
        rank += 1
    
    return rank if len(ranking) < P else -1

print(solution())