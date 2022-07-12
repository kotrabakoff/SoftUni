numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable number must be an integer")
    line = input()

line2 = input()

while line2 != "Remove":
    searched = line2
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in dictionary")
    line2 = input()

line3 = input()

while line3 != "End":
    searched = line3
    try:
        numbers_dictionary.pop(searched)
    except KeyError:
        print(f"Number does not exist in dictionary")
    line3 = input()

print(numbers_dictionary)
