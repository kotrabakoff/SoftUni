def Flip(a, b, c, d):
    if a == "Upper":
        new_string = d[:b] + d[b:c].upper() + d[c:]
        return new_string
    elif a == "Lower":
        new_string = d[:b] + d[b:c].lower() + d[c:]
        return new_string




raw_activation_key = input()
action = input()

while action != "Generate":
    action = action.split(">>>")
    command = action[0]
    if command == "Contains":
        substring = action[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        upper_lower = action[1]
        startIndex = int(action[2])
        endIndex = int(action[3])
        raw_activation_key = Flip(upper_lower, startIndex, endIndex, raw_activation_key)
        print(Flip(upper_lower, startIndex, endIndex, raw_activation_key))

    elif command == "Slice":
        startIndex2 = int(action[1])
        endIndex2 = int(action[2])
        raw_activation_key = raw_activation_key[:startIndex2] + raw_activation_key[endIndex2:]
        print(raw_activation_key)

    action = input()



print(f"Your activation key is: {raw_activation_key}")
