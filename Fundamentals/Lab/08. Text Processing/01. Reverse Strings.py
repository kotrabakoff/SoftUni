initial = input()

while initial != "end":
    rev =  reversed(initial)
    reversed_text = "".join(rev)
    print(f"{initial} = {reversed_text}")
    initial = input()
