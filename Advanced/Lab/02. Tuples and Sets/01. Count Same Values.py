initial = input().split()

numbers = [float(x) for x in initial]

ocurrances = {}

for i in numbers:
    if i not in ocurrances:
        ocurrances[i] = 1
    else:
        ocurrances[i] += 1

for x in ocurrances:
    print(f"{x} - {ocurrances[x]} times")

