from math import ceil

days = int(input())
kilometers = float(input())
sum = kilometers

for i in range(1, days+1):
    percent = int(input())
    kilometers += kilometers * percent/100
    sum += kilometers


if sum >= 1000:
    print(f"You've done a great job running {ceil(sum - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - sum)} more kilometers")