from os import remove
from os.path import exists

command = (input())

while command != "End":
    command = command.split("-")
    action = command[0]
    file = command[1]
    if action == "Create":
        current = open(f"{file}", "w")
    elif action == "Add":
        new_text = command[2]
        current = open(f"{file}", "a")
        current.write(new_text + '\n')
    elif action == "Replace":
        old_text = command[2]
        new_text = command[3]
        try:
            current = open(f"{file}", "r+")
            data = current.read()
            data = data.replace(old_text, new_text)
            current.seek(0)
            current.truncate()
            current.write(data)
        except:
            print("An error occurred")
            command = input()
            continue

    elif action == "Delete":
        if not exists(f"./{file}"):
            print("An error occurred")
            command = input()
            continue
        # file_to_close = open(f"{file}", "r")
        # file_to_close.close()
        remove(f"./{file}")
    command = input()

