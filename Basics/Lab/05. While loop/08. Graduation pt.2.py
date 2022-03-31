name = input()
grade = input()
sum = 0
n = 1
student = True

while n < 13:
    number = float(grade)
    sum = sum + number
    if number < 4:
        student = False
        break
    grade = input()
    n += 1

if student == True:
    print(f"{name} graduated. Average grade: {sum / 12:.2f}")
else:
    print(f"{name} has been excluded at {n} grade")