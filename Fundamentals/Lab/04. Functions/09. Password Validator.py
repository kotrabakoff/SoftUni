def Password_Validation(a):
    digits = 0
    nospecial = False
    twodigits = False
    length = False
    if 6 <= len(a) <= 10:
        length = True

    for i in a:
        if 47 < ord(i) < 58 or 64 < ord(i) < 91 or 96 < ord(i) < 123:
            nospecial = True

        else:
            nospecial = False
            break

    for i in a:
        if 47 < ord(i) < 58:
            digits += 1
            if digits >= 2:
                twodigits = True

    if length == False:
        print("Password must be between 6 and 10 characters")

    if nospecial == False:
        print("Password must consist only of letters and digits")

    if twodigits == False:
        print("Password must have at least 2 digits")

    if length == True and nospecial == True and twodigits == True:
        print("Password is valid")

password = input()

Password_Validation(password)