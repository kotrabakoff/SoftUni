times = int(input())

counter = 0
final_set = set()
evens = set()
odds = set()


for _ in range(times):
    name = list(f"{input()}")
    counter += 1
    sum_letters = 0
    for letter in name:
        sum_letters += ord(letter)
    final = sum_letters // counter
    if final % 2 == 1:
        odds.add(final)
    elif final % 2 == 0:
        evens.add(final)

if sum(odds) == sum(evens):
    final_print = list(odds.union(evens))
    print(*final_print, sep=", ")
elif sum(odds) > sum(evens):
    odds = list(odds)
    print(*odds, sep=", ")
elif sum(odds) < sum(evens):
    final_print = list(odds.union(evens))
    print(*final_print, sep=", ")
