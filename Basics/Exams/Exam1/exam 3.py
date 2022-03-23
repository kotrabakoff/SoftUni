country = input()
souvenir = input()
number = int(input())
price = 0


if country == "Argentina":
    if souvenir == "flags":
        price = number * 3.25
    elif souvenir == "caps":
        price = number * 7.2
    elif souvenir == "posters":
        price = number * 5.1
    elif souvenir == "stickers":
        price = number * 1.25

elif country == "Brazil":
    if souvenir == "flags":
        price = number * 4.20
    elif souvenir == "caps":
        price = number * 8.5
    elif souvenir == "posters":
        price = number * 5.35
    elif souvenir == "stickers":
        price = number * 1.2

elif country == "Croatia":
    if souvenir == "flags":
        price = number * 2.75
    elif souvenir == "caps":
        price = number * 6.9
    elif souvenir == "posters":
        price = number * 4.95
    elif souvenir == "stickers":
        price = number * 1.1

elif country == "Denmark":
    if souvenir == "flags":
        price = number * 3.1
    elif souvenir == "caps":
        price = number * 6.5
    elif souvenir == "posters":
        price = number * 4.80
    elif souvenir == "stickers":
        price = number * 0.9

if country not in ["Argentina", "Brazil", "Croatia", "Denmark"]:
    print("Invalid country!")
elif souvenir not in ["flags", "caps", "posters", "stickers"]:
    print("Invalid stock!")
else:
    print(f"Pepi bought {number} {souvenir} of {country} for {price:.2f} lv.")