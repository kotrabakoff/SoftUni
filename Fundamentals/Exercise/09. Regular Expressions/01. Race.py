import re

matches = []

while True:
    text = input()
    if not text:
        break
    matches = re.findall(r"\d+", text)
    if len(matches) > 0:
        final = " ".join(matches)
        print(final, end=" ")