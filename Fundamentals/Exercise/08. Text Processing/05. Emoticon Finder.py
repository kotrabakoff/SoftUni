text = input()
counter = 0

for i in text:
    if i == ":":
        current = text[counter + 1]
        print(f":{current}")
    counter += 1
