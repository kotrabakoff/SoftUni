import re

text = input()

regex = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))", text)

final = []

for i in regex:
    final.append(i.group())

print(" ".join(final))