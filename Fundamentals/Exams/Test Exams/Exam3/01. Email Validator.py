email = input()

action = input()

while action != "Complete":
    action = action.split(" ")
    command = action[0]
    if command == "Make":
        if action[1] == "Upper":
            email = email.upper()
            print(email)
        else:
            email = email.lower()
            print(email)
    elif command == "GetDomain":
        count = int(action[1])
        print(email[-count:])
    elif command == "GetUsername":
        if "@" in email:
            get_User_Split = email.split("@")
            print(get_User_Split[0])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command == "Replace":
        char = action[1]
        constant = "-"
        email = email.replace(char, constant)
        print(email)
    elif command == "Encrypt":
        for i in email:
            asc = ord(i)
            print(asc, end=" ")
    action = input()