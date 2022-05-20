def even_and_odd(a):
    evens = []
    odds = []
    for i in a:
        int_i = int(i)
        if (int_i % 2) == 0:
            evens.append(int_i)
        elif (int_i % 2) > 0:
            odds.append(int_i)
    evens_result = sum(evens)
    odds_result = sum(odds)
    print(f"Odd sum = {odds_result}, Even sum = {evens_result}")

string = input()

even_and_odd(string)