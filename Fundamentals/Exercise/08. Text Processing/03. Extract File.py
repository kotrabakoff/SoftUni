location = input().split("\\")

file = location[-1].split(".")

file_name = file[0]
extension = file[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
