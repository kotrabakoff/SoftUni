try:
    file = open("text.txt", 'r')
    print("File found")
except:
    print("File not found")