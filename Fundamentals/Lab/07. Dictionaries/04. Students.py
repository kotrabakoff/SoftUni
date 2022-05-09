students_data = input()
programming_basic = {}
fundamentals = {}
advanced = {}


while ":" in students_data:
    token = students_data.split(":")
    name = token[0]
    id = token[1]
    course = token[2]
    if course == "programming basics":
        programming_basic[name] = id

    elif course == "fundamentals":
        fundamentals[name] = id

    elif course == "advanced":
        advanced[name] = id
    students_data = input()

give_me = students_data


if give_me == "programming_basics":
    [print(f"{name} - {id}") for (name, id) in programming_basic.items()]

elif give_me == "fundamentals":
    [print(f"{name} - {id}") for (name, id) in fundamentals.items()]

elif give_me == "advanced":
    [print(f"{name} - {id}") for (name, id) in advanced.items()]