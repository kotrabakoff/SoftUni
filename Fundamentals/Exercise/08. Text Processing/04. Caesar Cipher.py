initial = input()
final_list = []

for i in initial:
    new_ascii = ord(i) + 3
    final_list.append(chr(new_ascii))

print("".join(final_list))

