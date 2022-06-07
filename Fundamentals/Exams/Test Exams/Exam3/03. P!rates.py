cities = input()
city_list = {}

while cities != "Sail":
    cities = cities.split("||")
    city = cities[0]
    people = int(cities[1])
    gold = int(cities[2])
    if city not in city_list:
        city_list[city] = [people, gold]
    else:
        city_list[city][0] += people
        city_list[city][1] += gold

    cities = input()

action = input()

while action != "End":
    disbanded = False
    action = action.split("=>")
    command = action[0]
    town = action[1]
    if command == "Plunder":
        people = int(action[2])
        gold = int(action[3])
        if city_list[town][0] - people >= 0:
            city_list[town][0] -= people
            current_people = people
            if city_list[town][0] == 0:
                disbanded = True
        else:
            current_people = people - city_list[town][0]
            city_list[town][0] = 0
            disbanded = True

        if town in city_list.keys():
            if city_list[town][1] - gold >= 0:
                city_list[town][1] -= gold
                current_gold = gold
                if city_list[town][1] == 0:
                    disbanded = True

            else:
                current_gold = gold - city_list[town][1]
                city_list[town][1] = 0
                disbanded = True

        print(f"{town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")

    elif command == "Prosper":
        gold = int(action[2])
        if gold >= 0:
            city_list[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_list[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    if disbanded == True:
        city_list.pop(town)
        print(f"{town} has been wiped off the map!")
    action = input()

print(f"Ahoy, Captain! There are {len(city_list.keys())} wealthy settlements to go to:")
for i in city_list.keys():
    print(f"{i} -> Population: {city_list[i][0]} citizens, Gold: {city_list[i][1]} kg")
