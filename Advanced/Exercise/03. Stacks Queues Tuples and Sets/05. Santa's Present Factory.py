from collections import deque
from collections import OrderedDict

material = [int(x) for x in input().split(" ")]
magic = deque([int(x) for x in input().split(" ")])

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

crafted = dict()

while material and magic:
    current_material = material.pop()
    current_magic = magic.popleft()
    multiplied = current_material * current_magic
    if current_magic == 0 and current_material == 0:
        continue
    if current_magic == 0 or current_material == 0:
        if current_magic == 0:
            material.append(current_material)
            continue
        elif current_material == 0:
            magic.appendleft(current_magic)
            continue

    if multiplied in presents.values():
        key = list(presents.keys())[list(presents.values()).index(multiplied)]
        if key in crafted.keys():
            crafted[key] += 1
        else:
            crafted[key] = 1
        continue
    if multiplied < 0:
        material.append(current_magic + current_material)
        continue
    if multiplied not in presents.values():
        material.append(current_material + 15)
        continue

if "Doll" and "Wooden train" in crafted or "Teddy bear" and "Bicycle" in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

final_material = [j for j in reversed([str(i) for i in material])]


if material:
    print(f"Materials left: {', '.join(final_material)}")

if magic:
    print(f"Magic left: {', '.join([str(i) for i in magic])}")

crafted = OrderedDict(sorted(crafted.items()))

for key, value in crafted.items():
    print(f"{key}: {value}")