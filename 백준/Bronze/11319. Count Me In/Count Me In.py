def count_vowels_and_consonants():
    import sys
    input = sys.stdin.read
    
    data = input().splitlines()
    S = int(data[0])  
    sentences = data[1:] 

    vowels = set('AEIOUaeiou') 

    results = []

    for sentence in sentences:
        vowel_count = 0
        consonant_count = 0

        for char in sentence:
            if char.isalpha():  
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        results.append(f"{consonant_count} {vowel_count}")

    print("\n".join(results))

count_vowels_and_consonants()
