initial = input()

counter = {}

for i in initial:
    if i in counter:
        counter[i] += 1
        continue
    counter[i] = 1

for key, value in sorted(counter.items()):
    print(f"{key}: {value} time/s")