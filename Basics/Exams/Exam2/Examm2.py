from math import ceil
from math import floor

days = int(input())
food = int(input())
first_food = float(input())
second_food = float(input())
third_food = float(input())

needed_food = days * (first_food + second_food + third_food)

if food >= needed_food:
    print(f"{floor(food - needed_food)} kilos of food left.")
else:
    print(f"{ceil(needed_food - food)} more kilos of food are needed.")