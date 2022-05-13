import re

text = input()

matches = re.finditer(r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})", text)

final_list = []

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")