number = int(input())

def line(line_number, number):
    start = (number - line_number) * " "
    for i in range(line_number):
        start += "* "
    line_to_be_returned = start

    return line_to_be_returned


def rhombus(number):
    counter = 0
    for i in range(number):
        counter += 1
        print(line(counter, number))

    for j in range(number-1, 0, -1):
        counter -= 1
        print(line(counter, number))

rhombus(number)