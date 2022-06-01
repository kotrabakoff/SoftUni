import re

text = input()
final = []
travel_points = 0
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

destinations = re.finditer(pattern, text)

for match in destinations:
    final.append(match.group(2))

for i in final:
    travel_points +=len(i)

print(f"Destinations: {', '.join(final)}")
print(f"Travel Points: {travel_points}")

