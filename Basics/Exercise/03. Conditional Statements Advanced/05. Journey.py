budget = float(input())
season = input()

location = 0
stay = 0
price = 0

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        stay = "Camp"
        price = budget * 0.3
    else:
        stay = "Hotel"
        price = budget * 0.7

elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        stay = "Camp"
        price = budget * 0.4
    else:
        stay = "Hotel"
        price = budget * 0.8

else:
    location = "Europe"
    stay = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {location}")
print(f"{stay} - {price:.2f}")
