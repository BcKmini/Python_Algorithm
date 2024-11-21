from itertools import combinations

def calculate_city_chicken_distance(houses, chicken_shops):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chicken_shops:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M = map(int, data[0].split())
    city_map = [list(map(int, line.split())) for line in data[1:]]

    houses = []
    chicken_shops = []

    for r in range(N):
        for c in range(N):
            if city_map[r][c] == 1:
                houses.append((r, c))
            elif city_map[r][c] == 2:
                chicken_shops.append((r, c))
    
    min_city_distance = float('inf')
    for selected_chickens in combinations(chicken_shops, M):
        city_distance = calculate_city_chicken_distance(houses, selected_chickens)
        min_city_distance = min(min_city_distance, city_distance)

    print(min_city_distance)

if __name__ == "__main__":
    main()
