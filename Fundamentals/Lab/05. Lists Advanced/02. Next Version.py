def Next_Version(a):
    version = list(map(int, a.split(".")))
    if version[-1] == 9:
        if version[1] == 9:
            version[0] += 1
            version[1] = 0
            version[-1] = 0
        else:
            version[1] += 1
            version[-1] = 0
    else:
        version[-1] += 1
    final = ".".join(list(map(str, version)))
    return final

current_version = input()

print(Next_Version(current_version))