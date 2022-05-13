string = input()
numbers = ""
letters = ""
signs = ""

for ch in string:
    if ch.isdigit():
        numbers += ch
    elif ch.isupper() or ch.islower():
        letters += ch
    else:
        signs += ch

print(numbers)
print(letters)
print(signs)

