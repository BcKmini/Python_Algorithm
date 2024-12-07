def count_over(document, word):
    count = 0
    index = 0

    while index <= len(document) - len(word):
        if document[index:index+len(word)] == word:
            count += 1
            index += len(word)
        else:         
            index += 1
    return count

document = input().strip()
word = input().strip()

print(count_over(document, word))
