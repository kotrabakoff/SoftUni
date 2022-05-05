def Palindrome(a, word):
    counter = 0
    list = []
    for i in a:
        if i == "".join(reversed(i)):
            list.append(i)

    print(list)
    print(f"Found palindrome {list.count(word)} times")

all_words = input().split()
searched_palindrome = input()

Palindrome(all_words, searched_palindrome)