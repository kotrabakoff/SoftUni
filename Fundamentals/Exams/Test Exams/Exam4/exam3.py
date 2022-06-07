action = input()
distributors = {}
clients = {}
total = float()

while action != "End":
    action = action.split(" ")
    command = action[0]
    if command == "Deliver":
        distributor_Name = action[1]
        money_Spent = float(action[2])
        if distributor_Name not in distributors:
            distributors[distributor_Name] = money_Spent
        else:
            distributors[distributor_Name] += money_Spent

    elif command == "Return":
        distributor_Name2 = action[1]
        money_Returned = float(action[2])
        if distributor_Name2 in distributors:
            if distributors[distributor_Name2] < money_Returned:
                action = input()
                continue
            distributors[distributor_Name2] -= money_Returned
            if distributors[distributor_Name2] <= 0:
                distributors.pop(distributor_Name2)

    elif command == "Sell":
        client_Name = action[1]
        money_Earned = float(action[2])
        total += float(money_Earned)
        if client_Name not in clients:
            clients[client_Name] = money_Earned
        else:
            clients[client_Name] += money_Earned
    action = input()

for i in clients.keys():
    print(f"{i}: {clients[i]:.2f}")

print("-----------")

for j in distributors.keys():
    print(f"{j}: {distributors[j]:.2f}")

print("-----------")

print(f"Total Income: {total:.2f}")


