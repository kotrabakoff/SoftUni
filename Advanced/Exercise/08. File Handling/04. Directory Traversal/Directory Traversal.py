from os import listdir
from os.path import isdir, join

def traversal(path, ext):
    for i in listdir(path):
        if isdir(join(path, i)):
            traversal(join(path, i), ext)
        else:
            extension = i.split(".")[-1]
            if extension not in ext:
                ext[extension] = []
            ext[extension].append(i)

result = {}
traversal("./", result)

for key in result.keys():
    print(f".{key}")
    for j in result[key]:
        print(f"---{j}")