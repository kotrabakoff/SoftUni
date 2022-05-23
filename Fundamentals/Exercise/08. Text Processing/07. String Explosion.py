text = input()
counter = 0
final = []
times_to_remove = 0

for i in text:
    if i == ">":
        times_to_remove += int(text[counter + 1])
        final.append(i)
        counter += 1
        continue
    else:
        if times_to_remove > 0:
            times_to_remove -= 1
            counter += 1
            continue
        else:
            final.append(i)
    counter += 1

print("".join(final))



