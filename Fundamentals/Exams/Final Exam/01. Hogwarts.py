# text = input().split()
# spell = input().split(" ")
# final = ""
#
# while spell != "Abracadabra":
#     command = spell[0]
#     if command == "Abjuration":
#         text = [x.upper() for x in text]
#     elif command == "Necromancy":
#         text = [x.lower() for x in text]
#
#     elif command == "Illusion":
#         index = spell[1]
#         letter_to_replace = text[index]
#         letter = spell[2]
#         text = text[:letter_to_replace] + letter + text[letter_to_replace + 1:]
#         print("Done!")
#     elif command == "Divination":
#         first_substring = spell[1]
#         second_substring = spell[2]
#         if first_substring in final:
#             final.replace(first_substring, second_substring)
#         else:
#             continue
#     elif command == "Alteration":
#         substring = spell[1]
#         if substring in final:
#             final.remove(substring)
#     spell = input()
#
# print(final)


text = input()
command = input()

while command != "Abracadabra":
    command = command.split(" ")
    spell = command[0]
    if spell == "Abjuration":
        text = text.upper()
        print(text)
    elif spell == "Necromancy":
        text = text.lower()
        print(text)
    elif spell == "Illusion":
        index = int(command[1])
        letter = command[2]
        if 0 <= index <= len(text):
            text = text[:index] + letter + text[index+1:]
            print("Done")
        else:
            print("The spell was too weak.")
    elif spell == "Divination":
        first_substring = command[1]
        second_substring = command[2]
        if first_substring in text:
            text.replace(first_substring, second_substring)
            print(text)
    elif spell == "Alteration":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, " ")
    else:
        print("The spell did not work!")
    command = input()


print(text)

