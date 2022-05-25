initial = list(input().split(", "))
whole_command = input()

while whole_command != "End":
    command_list = whole_command.split(" - ")
    whole_command = input()
    command = command_list[0]
    phone = command_list[1]
    if command == "Add":
        if phone in initial:
            continue
        else:
            initial.append(phone)
    elif command == "Remove":
        if phone in initial:
            initial.remove(phone)
        else:
            continue
    elif command == "Bonus phone":
        bonus_split = phone.split(":")
        old_Phone = bonus_split[0]
        new_Phone = bonus_split[1]
        if old_Phone in initial:
            index = initial.index(old_Phone)
            initial.insert(index+1, new_Phone)
        else:
            continue
    elif command == "Last":
        if phone in initial:
            # index = initial.index(phone)
            initial.remove(phone)
            initial.append(phone)
        else:
            continue

string = ", ".join(str(i) for i in initial)

print(string)

