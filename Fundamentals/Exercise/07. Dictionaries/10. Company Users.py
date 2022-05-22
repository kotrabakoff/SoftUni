initial = input()
final_dict = dict()

while initial != "End":
    initial = initial.split(" -> ")
    company = initial[0]
    name = initial[1]
    if company not in final_dict:
        final_dict[company] = []
        final_dict[company].append(name)
    else:
        if name in final_dict[company]:
            initial = input()
            continue
        else:
            final_dict[company].append(name)
    initial = input()

for i in final_dict:
    print(f"{i}")
    for j in final_dict[i]:
        print(f"-- {j}")

