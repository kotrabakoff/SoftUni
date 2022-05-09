count = int(input())
dictionary = {}

for i in range(count):
    word = input()
    possible_synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(possible_synonym)

for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
