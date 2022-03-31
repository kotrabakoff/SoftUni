import sys

number = input()
min = sys.maxsize

while number != "Stop":
    next_number = int(number)
    if next_number < min:
        min = next_number
    number = input()

print(min)