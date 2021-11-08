st = input()
target = input()

string = ""
for char in st:
    if ord(char) < ord('0') or ord(char) > ord('9'):
        string += char
print(int(target in string))
