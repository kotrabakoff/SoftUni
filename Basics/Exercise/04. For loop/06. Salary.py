
tabs = int(input())
salary = float(input())

for number in range(tabs):
    currentTab = input()
    if currentTab == "Facebook":
        salary -= 150
    elif currentTab == "Instagram":
        salary -= 100
    elif currentTab == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{int(salary)}")