from os import remove

# file = open('my_first_file.txt', 'w')
# file.write('I just created my first file!')
# file.close()

try:
    remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')