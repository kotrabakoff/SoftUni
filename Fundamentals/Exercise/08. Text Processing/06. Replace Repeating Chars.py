text = input()
count = 0
final_list = []

for i in text:
    if count + 1 == len(text):
        final_list.append(i)
        break
    elif i != text[count + 1]:
        count += 1
        final_list.append(i)
    elif i == text[count + 1]:
        count += 1
        continue

print("".join(final_list))