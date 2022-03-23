from math import floor

number_of_companies = int(input())
best = 0
best_company = 0
average = 0


for iteration in range(1, number_of_companies+1):
    company = input()
    command = input()
    sum = 0
    counter = 0
    while command != "Finish":
        passengers = int(command)
        counter += 1
        sum = sum + passengers
        command = input()
    average = sum / counter
    if average > best:
        best_company = company
        best = average
    print(f"{company}: {floor(average)} passengers.")

print(f"{best_company} has most passengers per flight: {best}")