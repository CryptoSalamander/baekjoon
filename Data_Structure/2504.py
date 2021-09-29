st = input().rstrip()

stack = []
is_opened = True
not_valid = False
for char in st:
    if char == '(' or char == '[':
        stack.append(char)
        is_opened = True
    else:
        if char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                is_opened = False
            elif not stack:
                not_valid = True
        else:
            if stack and stack[-1] == '[':
                stack.pop()
                is_opened = False
            elif not stack:
                not_valid = True
if stack or is_opened:
    not_valid = True

if not_valid:
    print(0)
else:
    answer = []
    for char in st:
        if char == '(':
            answer.append('(')
        if char == ')':
            if answer[-1] == '(':
                answer.pop()
                answer.append(2)
            else:
                tmp = 0
                while(True):
                    a = answer.pop()
                    if a == '(':
                        answer.append(tmp*2)
                        break
                    else:
                        tmp += a
        if char == '[':
            answer.append('[')
        if char == ']':
            if answer[-1] == '[':
                answer.pop()
                answer.append(3)
            else:
                tmp = 0
                while(True):
                    a = answer.pop()
                    if a == '[':
                        answer.append(tmp*3)
                        break
                    else:
                        tmp += a
    print(sum(answer))

