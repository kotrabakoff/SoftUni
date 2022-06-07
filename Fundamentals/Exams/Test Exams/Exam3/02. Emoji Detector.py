import re

text = input()

numbers = re.findall(r"\d", text)

multiplied = 1
for i in numbers:
    multiplied *= int(i)
print(f"Cool threshold: {multiplied}")

pattern = r"(\*\*|\:\:)([A-Z][a-z]{2,})(\1)"
matches_list = []

matches = re.finditer(pattern, text)

for j in matches:
    matches_list.append(j.group(2))

print(f"{len(matches_list)} emojis found in the text. The cool ones are:")

matches2 = re.finditer(pattern, text)

for l in matches2:
    elem = l.group(2)
    current = 0
    for k in elem:
        current += int(ord(k))
    if current > multiplied:
        print(f"{l.group(1)}{l.group(2)}{l.group(3)}")