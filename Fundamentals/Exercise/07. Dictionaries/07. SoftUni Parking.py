times = int(input())

registered = {}

for i in range(0, times):
    initial = input()
    initial = initial.split(" ")
    if initial[0] == "register":
        if initial[1] in registered:
            print(f"ERROR: already registered with plate number {registered[initial[1]]}")
        else:
            registered[initial[1]] = initial[2]
            print(f"{initial[1]} registered {registered[initial[1]]} successfully")
    elif initial[0] == "unregister":
        if initial[1] not in registered:
            print(f"ERROR: user {initial[1]} not found")
        else:
            registered.pop(initial[1])
            print(f"{initial[1]} unregistered successfully")


for key, value in registered.items():
    test_string = f"{key} => {value}"
    print(f"{test_string}")

