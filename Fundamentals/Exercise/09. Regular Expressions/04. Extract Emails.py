import re

text = input()
final = []

user = "[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*"
host = "[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

matches = re.finditer(rf"{user}@{host}", text)

for i in matches:
    print(i[0])

