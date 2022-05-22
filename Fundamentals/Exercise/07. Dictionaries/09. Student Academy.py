times = int(input())
all_grades = dict()

for i in range(0, 2*times, 2):
    key = input()
    value = float(input())
    if key in all_grades:
        all_grades[key].append(value)
    else:
        all_grades[key] = []
        all_grades[key].append(value)

for key in all_grades:
    average = sum(all_grades[key]) / len(all_grades[key])
    if average >= 4.5:
        print(f'{key} -> {average:.2f}')