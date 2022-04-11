steps = input()
sum = 0
difference = 0
goal_reached = False

while steps != "Going home":
    steps = int(steps)
    sum = sum + steps
    if sum >= 10000:
        goal_reached = True
        break
    steps = input()

if steps == "Going home":
    steps = int(input())
    sum = sum + steps
    if sum >= 10000:
        goal_reached = True

if goal_reached == False:
    print(f"{abs(sum - 10000)} more steps to reach goal.")
elif goal_reached == True:
    print(f"Goal reached! Good job!")
    print(f"{sum - 10000} steps over the goal!")


