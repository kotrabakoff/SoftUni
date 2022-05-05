def Happiness(a):
    average = sum(a) / len(a)
    happy_people = []
    for i in a:
        if i >= average:
            happy_people.append(i)
    half = int(len(a) / 2)
    if len(happy_people) >= half:
        print(f"Score: {len(happy_people)}/{len(a)}. Employees are happy!")
    else:
        print(f"Score: {len(happy_people)}/{len(a)}. Employees are not happy!")

initial = list(map(int, input().split(" ")))
factor = int(input())

employees = [i * factor for i in initial]

Happiness(employees)
