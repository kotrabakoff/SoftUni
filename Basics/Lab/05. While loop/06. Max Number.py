import sys

number = input()
max = -sys.maxsize

while number != "Stop":
    next_number = int(number)
    if next_number > max:
        max = next_number
    number = input()

print(max)