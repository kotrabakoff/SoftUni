destinations = input()
text = input()

while text != "Travel":
    text = text.split(":")
    command = text[0]
    if command == "Add Stop":
        index = int(text[1])
        place = text[2]
        destinations = destinations[:index] + place + destinations[index:]
    elif command == "Remove Stop":
        index1 = int(text[1])
        index2 = int(text[2])
        if len(destinations) >= index1 and len(destinations) >= index2:
            destinations = destinations[:index1] + destinations[index2 + 1:]
    elif command == "Switch":
        country1 = text[1]
        country2 = text[2]
        destinations = destinations.replace(country1, country2)
    print(destinations)
    text = input()

print(f"Ready for world tour! Planned stops: {destinations}")