bought_food = int(input())
command = input()

food_in_grams = bought_food * 1000
sum = 0
number = 0

while command != "Adopted":
    number = int(command)
    sum = sum + number
    command = input()

if food_in_grams >= sum:

    print(f"Food is enough! Leftovers: {food_in_grams - sum } grams.")
else:
    print(f"Food is not enough. You need {sum - food_in_grams} grams more.")