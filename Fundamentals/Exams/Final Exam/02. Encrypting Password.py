import re

times = int(input())

for i in range(0,times):
    text = input()
    regex = re.match(r"(?P<first>\D+)>(?P<numbers>\d+)[|](?P<lower>[a-z]+)[|](?P<upper>[A-Z]+)[|](?P<symbols>\W+|\D+)<\1$", text)
    if regex is not None:
        final = regex[2] + regex[3] + regex[4] + regex [5]
        print(f"Password: {final}")
    else:
        print("Try another password!")


