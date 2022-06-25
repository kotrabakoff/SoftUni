repeats = int(input())

all = {}

for i in range(repeats):
    result = input().split()
    name = result[0]
    grade = float(result[1])
    if name not in all:
        all[name] = []
    all[name].append(grade)

#
# for x in all:
#     grades_formated = ' '.join(f"{all[x]:.2f}" for all[x])
#     print(f"{x} -> {current} (avg: {(sum(all[x])/len(all[x])):.2f})")

for student, grades in all.items():
    formatted = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {formatted} (avg: {sum(grades)/len(grades):.2f})")