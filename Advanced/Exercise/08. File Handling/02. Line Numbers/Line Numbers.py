import re
from string import punctuation

counter = 0
pattern = "[A-Za-z]"

new_file = open("output.txt", "w")

with open("text.txt", "r") as file:
    for line in file:
        number_of_signs = 0
        counter += 1
        letters = re.findall(pattern, line)
        for j in line:
            if j in punctuation:
                number_of_signs += 1
        new_file.write(f"Line {counter}: {line}({len(letters)})({number_of_signs})\n")