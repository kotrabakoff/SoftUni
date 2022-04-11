from math import floor

number_of_companies = int(input())
company = input()
best = 0
best_company = 0
average = 0


for iteration in range(0, number_of_companies):
    passengers = input()
    sum = 0
    counter = 0

    while passengers != "Finish":
        passengers = int(passengers)
        counter += 1
        sum = sum + passengers
        passengers = input()
    average = sum / counter
    if average > best:
        best_company = company
        best = average
    print(f"{company}: {floor(average)} passengers.")
    company = input()
    if counter == number_of_companies:
        break

print(f"{best_company} has most passengers per flight: {best}")