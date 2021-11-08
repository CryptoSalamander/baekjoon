st = input()
check = False
tag = []
answer = []
string = []
for char in st:
    if char == '<':
        check = True
        string.reverse()
        answer.append(string)
        string = []
        tag.append(char)
    elif char == '>':
        tag.append(char)
        answer.append(tag)
        check = False
        tag = []
    elif char == ' ':
        if check:
            tag.append(char)
        else:
            string.reverse()
            answer.append(string)
            answer.append([' '])
            string = []
    else:
        if check:
            tag.append(char)
        else:
            string.append(char)
string.reverse()
answer.append(string)
for item in answer:
    print("".join(item),end='')
