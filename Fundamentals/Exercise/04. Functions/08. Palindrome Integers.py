def Palindrome(a):
    for i in a:
        if i == i[::-1]:
            print("True")
        else:
            print("False")

numbers = list(input().split(", "))

Palindrome(numbers)