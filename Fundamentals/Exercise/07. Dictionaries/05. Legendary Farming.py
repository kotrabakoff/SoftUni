current_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

item_obtained = False

while item_obtained == False:
    initial = input()
    materials = initial.lower()
    materials_list = materials.split(" ")
    for i in range(0, len(materials_list), 2):
        if item_obtained == True:
            break
        value = int(materials_list[i])
        key = materials_list[i + 1]
        if key in ["shards", "fragments", "motes"]:
            current_dict[key.lower()] += value
        else:
            if key not in junk:
                junk[key] = value
            else:
                junk[key] += value
        for key in current_dict:
            if current_dict[key] >= 250:
                item_obtained = True
                break

sufficient_element_list = [key for key, value in current_dict.items() if value >= 250]

sufficient_element = ''.join(sufficient_element_list)

if sufficient_element == "shards":
    current_dict["shards"] -= 250
    print(f"Shadowmourne obtained!")
elif sufficient_element == "fragments":
    current_dict["fragments"] -= 250
    print(f"Valanyr obtained!")
elif sufficient_element == "motes":
    current_dict["motes"] -= 250
    print(f"Dragonwrath obtained!")

for key in current_dict:
    print(f"{key}: {current_dict[key]}")

for key in junk:
    print(f"{key}: {junk[key]}")
