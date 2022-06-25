initial = input().split(" ")

initial = [int(x) for x in initial]

summ = int(input())

final = set()
pairs = set()

current = list(initial)
iterations = 0

for i in initial:
    current.pop(0)
    for j in current:
        iterations += 1
        if i + j == summ:
            # final.add(f"{i} + {j} = {summ}")
            print((f"{i} + {j} = {summ}"))
            pairs.add((i, j))
        else:
            continue

print(f"Iterations done: {iterations}")
for x in pairs:
    print(x)
