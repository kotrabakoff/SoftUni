initial = input()
all_items = []
separated_items = {}

while initial != "stop":
    all_items.append(initial)
    initial = input()

for i in range(0, len(all_items), 2):
    key = all_items[i]
    value = int(all_items[i+1])
    if key not in separated_items:
        separated_items[key] = value
    else:
        separated_items[key] += value

for key in separated_items:
    print(f"{key} -> {separated_items[key]}")