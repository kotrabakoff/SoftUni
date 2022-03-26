sea = int(input())
mountain = int(input())
sea_sold = False
mountain_sold = False
command = input()
profit_sea = 0
profit_mountain = 0

while command != "Stop":
    if command == "sea":
        if sea > 0:
            profit_sea += 680
            sea -= 1
    elif command == "mountain":
        if mountain > 0:
            profit_mountain += 499
            mountain -= 1

    if mountain == 0 and sea == 0:
        print(f"Good job! Everything is sold.")
        break
    command = input()

profit = profit_sea + profit_mountain

print(f"Profit: {profit} leva.")


