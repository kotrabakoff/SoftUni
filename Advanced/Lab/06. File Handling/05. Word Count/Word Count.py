import re

regex = r'\b\S+\b'

def read_words():
    with open('words.txt', 'r') as file:
        return file.read().split(' ')

def count_words_in_file(words):
    words_count = {
        word: 0 for word in words
    }

    with open('input.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(regex, line)]
            for word in words:
                words_count[word] += words_in_line.count(word)
    return words_count



final = count_words_in_file(read_words())

for key in final.keys():
    print(f"{key} - {final[key]}")



# final = dict()
#
# for i in file:
#     current = (file2.readlines()).lower()
#     if i in current:
#         if i in final:
#             final[i] += 1
#         else:
#             final[i] = 1
#
# for key, value in final:
#     print(f"{key} = {value}")

