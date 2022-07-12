import re

to_be_replaced = {"-", ",", ".", "!", "?"}
regex = r'\b\S+\b'


def text_manipulator():
    counter = 0
    final = []
    with open('text.txt', 'r') as file:
        for line in file:
            if counter % 2 == 1:
                counter += 1
                continue
            line = line.strip()
            backwards = ' '.join(line.strip().split()[::-1])
            for symbol in to_be_replaced:
                if symbol in backwards:
                    backwards = backwards.replace(symbol, "@")
            final.append(backwards)
            counter += 1
        return final


for j in text_manipulator():
    print(j)