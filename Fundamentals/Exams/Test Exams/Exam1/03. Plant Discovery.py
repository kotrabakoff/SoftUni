n = int(input())
rarity_dict = {}
rating_dict = {}

for i in range(0, n):
    text = input().split("<->")
    plant = text[0]
    rarity = int(text[1])
    rarity_dict[plant] = rarity

rarity_text = input()

while rarity_text != "Exhibition":
    rarity_text = rarity_text.split(": ")
    command = rarity_text[0]
    rarity_text = rarity_text[1].split(" - ")
    plant = rarity_text[0]
    if plant not in rarity_dict:
        print("error")
        rarity_text = input()
        continue

    if command == "Rate":
        rating = int(rarity_text[1])
        if plant in rating_dict:
            rating_dict[plant].append(rating)
        else:
            rating_dict[plant] = list()
            rating_dict[plant].append(rating)
    elif command == "Update":
        rarity_update = int(rarity_text[1])
        rarity_dict[plant] = rarity_update
    elif command == "Reset":
        rating_dict[plant] = 0
    rarity_text = input()

print(f"Plants for the exhibition:")
for plant in rarity_dict:
    if rating_dict[plant] == 0:
        print(f"- {plant}; Rarity: {rarity_dict[plant]}; Rating: {rating_dict[plant]:.2f}")
    else:
        print(f"- {plant}; Rarity: {rarity_dict[plant]}; Rating: {sum(rating_dict[plant]) / len(rating_dict[plant]):.2f}")


