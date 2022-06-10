parantheses = input()

parantheses = [x for x in parantheses]

balanced = False
index = 0
for i in parantheses:
    index = parantheses.index(i) + 1
    if i == "(":
        if parantheses[-index] == ")":
            balanced = True
            parantheses.pop
        else:
            balanced = False
            break
    if parantheses[-index] == "{":
        if "}" in parantheses:
            balanced = True
        else:
            balanced = False
            break
    if parantheses[-index] == "[":
        if "]" in parantheses:
            balanced = True
        else:
            balanced = False
            break

if balanced == True:
    print("YES")
else:
    print("NO")
