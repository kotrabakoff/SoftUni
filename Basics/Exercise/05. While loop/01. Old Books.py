needed_book = input()
books_available = input()
found = False
books_count = 0

while books_available != "No More Books":
    if books_available == needed_book:
        found = True
        print(f"You checked {books_count} books and found it.")
        break
    books_available = input()
    books_count += 1

if found != True:
    print(f"The book you search is not here!")
    print(f"You checked {books_count} books.")