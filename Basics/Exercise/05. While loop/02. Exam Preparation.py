limit_bad_grades = int(input())
bad_grade_count = 0
exercise_count = 0
sum = 0
last_exercise = ""
has_failed = True

while bad_grade_count < limit_bad_grades:
    exercise = input()
    if exercise == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        bad_grade_count += 1
    sum += grade
    exercise_count += 1
    last_exercise = exercise

if has_failed:
    print(f"You need a break, {limit_bad_grades} poor grades.")
else:
    print(f"Average score: {sum / exercise_count:.2f}")
    print(f"Number of problems: {exercise_count}")
    print(f"Last problem: {last_exercise}")
