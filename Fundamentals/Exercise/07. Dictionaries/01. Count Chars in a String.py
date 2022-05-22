text = input()
characters = dict()

for i in text:
    if i != " ":
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1

for i in characters:
    print(f"{i} -> {characters[i]}")

