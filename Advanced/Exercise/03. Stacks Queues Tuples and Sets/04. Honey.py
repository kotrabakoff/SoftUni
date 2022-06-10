from collections import deque

bees_all = deque([int(x) for x in input().split(" ")])
nectar_all = [int(x) for x in input().split(" ")]
operators = deque(input().split())

symbols = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

honey_collected = 0

while bees_all and nectar_all:
    bee = bees_all.popleft()
    nectar = nectar_all.pop()

    if nectar < bee:
        bees_all.appendleft(bee)
        continue
    if nectar == 0:
        continue

    operator = operators.popleft()
    honey_collected += abs(symbols[operator](bee, nectar))


print(f"Total honey made: {honey_collected}")
if bees_all:
    print(f"Bees left: {', '.join(map(str, (bees_all)))}")
if nectar_all:
    print(f"Nectar left: {', '.join(map(str, (nectar_all)))}")



