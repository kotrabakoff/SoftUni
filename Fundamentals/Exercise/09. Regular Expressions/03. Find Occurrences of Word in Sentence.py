import re

text = input()
word = input()

matches = re.findall(rf"\b{word}\b", text, re.IGNORECASE)

print(len(matches))