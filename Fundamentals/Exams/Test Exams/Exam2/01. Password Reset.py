def TakeOdd(a):
    current_list = []
    for i in range(len(a)):
        if i % 2 == 1:
            current_list.append(a[i])
    new_text = f"".join(current_list)
    return new_text

def Cut(a, b, c):
    new_text2 = c[:a] + c[(a+b):]
    return new_text2

def Substitute(a, b, c):
    if a in c:
        new_text3 = c.replace(a, b)
        return new_text3
    else:
        print("Nothing to replace!")


text = input()
action = input()

while action != "Done":
    action = action.split()
    command = action[0]
    if command == "TakeOdd":
        print(TakeOdd(text))
        text = TakeOdd(text)
    elif command == "Cut":
        index = int(action[1])
        length = int(action[2])
        print(Cut(index, length, text))
        text = Cut(index, length, text)
    elif command == "Substitute":
        substring = action[1]
        substitute = action[2]
        if substring in text:
            print(Substitute(substring, substitute, text))
            text = Substitute(substring, substitute, text)
        else:
            Substitute(substring, substitute, text)
    action = input()

print(f"Your password is: {text}")