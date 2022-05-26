text = input()
animals = {}

while text != "EndDay":
    text = text.split(": ")
    command = text[0]
    text = text[1].split("-")
    animal = text[0]
    if command == "Add":
        needed_food = int(text[1])
        area = text[2]
        if animal not in animals:
            animals[animal] = [needed_food, area]
        else:
            animals[animal][0] += needed_food
    elif command == "Feed":
        food = text[1]
        if animal in animals:
            animals[animal] -= food
        else:
            continue
        for animal, needed_food in animals:
            if needed_food == 0:
                animals.pop(animal)
                print(f"{animal} was successfully fed")
    text = input()



print("Animals:")
for animal in animals.keys():
    print(f"{animal} -> {animals[animal]}g")

print(f"Areas with hungry animals:")
for animal in animals.keys():
    print(f"{animals[animal][0]}")