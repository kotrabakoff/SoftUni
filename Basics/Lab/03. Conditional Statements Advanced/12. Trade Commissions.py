    town = input()
    sales = float(input())

    if town == "Sofia":
        if 0 <= sales <= 500:
            commision = sales * 0.05
            print(f"{commision:.2f}")
        elif 500 <= sales <= 1000:
            commision = sales * 0.07
            print(f"{commision:.2f}")
        elif 1000 <= sales <= 10000:
            commision = sales * 0.08
            print(f"{commision:.2f}")
        elif sales > 10000:
            commision = sales * 0.12
            print(f"{commision:.2f}")
        else:
            print("error")

    elif town == "Varna":
        if 0 <= sales <= 500:
            commision = sales * 0.045
            print(f"{commision:.2f}")
        elif 500 <= sales <= 1000:
            commision = sales * 0.075
            print(f"{commision:.2f}")
        elif 1000 <= sales <= 10000:
            commision = sales * 0.1
            print(f"{commision:.2f}")
        elif sales > 10000:
            commision = sales * 0.13
            print(f"{commision:.2f}")
        else:
            print("error")

    elif town == "Plovdiv":
        if 0 <= sales <= 500:
            commision = sales * 0.055
            print(f"{commision:.2f}")
        elif 500 <= sales <= 1000:
            commision = sales * 0.08
            print(f"{commision:.2f}")
        elif 1000 <= sales <= 10000:
            commision = sales * 0.12
            print(f"{commision:.2f}")
        elif sales > 10000:
            commision = sales * 0.145
            print(f"{commision:.2f}")
        else:
            print("error")

    else:
        print("error")