a = float(input())

if a == 0:
    print("zero")
elif a > 0:
    if a < 1:
        print("small positive")
    elif a > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if a > -1:
        print("small negative")
    elif -1000000 < a < -1:
        print("negative")
    else:
        print("large negative")