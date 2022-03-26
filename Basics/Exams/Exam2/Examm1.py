people = int(input())
nights = int(input())
card = int(input())
tickets = int(input())

sum = people * (nights * 20 + card * 1.6 + tickets * 6)

total = sum + (sum * 0.25)

print(f"{total:.2f}")