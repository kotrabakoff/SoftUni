initial = input()
course_dict = dict()

while initial != "end":
    initial = initial.split(" : ")
    course = initial[0]
    name = initial[1]
    if course in course_dict:
        course_dict[course].append(name)
    else:
        course_dict[course] = []
        course_dict[course].append(name)

    initial = input()

for i in course_dict:
    print(f"{i}: {len(course_dict[i])}")
    for j in course_dict[i]:
        print(f"-- {j}")

