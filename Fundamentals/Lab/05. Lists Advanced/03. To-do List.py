todo = ["" for i in range(11)]
initial = input()

while initial != "End":
    initial = initial.split("-")
    place = int(initial[0])
    action = initial[1]
    todo[place] = action
    initial = input()

final_todo = [i for i in todo if i != ""]
print(final_todo)



# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split("-")
#     priority = int(tokens[0]) - 1
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# print(notes)