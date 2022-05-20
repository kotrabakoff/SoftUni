def Decipher(a):
    number = []
    final = []
    for i in a:
        letter_list = list(i)
        for j in i:
            if j.isdigit():
                number.append(int(j))
                letter_list.remove(j)
        letter_rest = "".join(letter_list)
        ascii_Number = int("".join(map(str, number)))
        first_letter = chr(ascii_Number)
        word = first_letter + letter_rest
        final_list = list(word)
        final_list[1], final_list[-1] = final_list[-1], final_list[1]
        final_word = "".join(final_list)
        final.append(final_word)
        number = []
    print(F"{' '.join(final)}")

initial = input().split(" ")
Decipher(initial)