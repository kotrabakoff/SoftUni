import re

text = input()

matches = re.findall(r"\b_[0-1A-Za-z]+\b", text)

for i in matches:
    if i == matches[-1]:
        print(i[1::])
    else:
        print(i[1::], end=",")

