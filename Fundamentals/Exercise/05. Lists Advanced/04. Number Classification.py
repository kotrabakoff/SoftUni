def Classification(a):
    positives = []
    negatives = []
    evens = []
    odds = []
    for i in a:
        if i >= 0:
            positives.append(i)
        else:
            negatives.append(i)
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"Positive: {', '.join(list(map(str, positives)))}")
    print(f"Negative: {', '.join(list(map(str, negatives)))}")
    print(f"Even: {', '.join(list(map(str, evens)))}")
    print(f"Odd: {', '.join(list(map(str, odds)))}")

initial = list(map(int, input().split(", ")))

Classification(initial)