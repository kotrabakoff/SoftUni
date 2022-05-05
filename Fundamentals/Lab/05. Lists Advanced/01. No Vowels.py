def Remove_Vowels(a):
    vowels = ["a", "o", "u", "e", "i",]
    result = [i for i in a if i not in vowels]
    return result

initial = input()

print("".join(Remove_Vowels(initial)))



