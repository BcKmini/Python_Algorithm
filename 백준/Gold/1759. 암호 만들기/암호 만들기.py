from itertools import combinations

L, C = map(int, input().split())
characters = input().split()

vowels = {'a', 'e', 'i', 'o', 'u'}

characters.sort()

possible_combinations = combinations(characters, L)

for combination in possible_combinations:
    vowel_count = sum(1 for char in combination if char in vowels)
    consonant_count = L - vowel_count
    
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(combination))
