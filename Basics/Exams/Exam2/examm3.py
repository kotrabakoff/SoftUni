
people = int(input())
season = input()

if people <= 5:
    if season == "spring":
        total = people * 50
    elif season == "summer":
        total = (people * 48.5) - ((people * 48.5) * 0.15)
    elif season == "autumn":
        total = people * 60
    else:
        total = (people * 86) + ((people * 86) * 0.08)
else:
    if season == "spring":
        total = people * 48
    elif season == "summer":
        total = (people * 45) - ((people * 45) * 0.15)
    elif season == "autumn":
        total = people * 49.5
    else:
        total = (people * 85) + ((people * 85) * 0.08)

print(f"{total:.2f} leva.")