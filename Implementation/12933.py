st = input()
stack_list = []

if st[0] != 'q':
    print(-1)
    exit()
stack_list.append(['q'])

for char in st[1:]:
    is_valid = False
    if char == 'q':
        for stack in stack_list:
            if stack[-1] == 'k':
                stack.append(char)
                is_valid = True
                break
        if not is_valid:
            stack_list.append(['q'])
    elif char == 'u':
        for stack in stack_list:
            if stack[-1] == 'q':
                stack.append(char)
                is_valid = True
                break
        if not is_valid:
            print(-1)
            exit()
    elif char == 'a':
        for stack in stack_list:
            if stack[-1] == 'u':
                stack.append(char)
                is_valid = True
                break
        if not is_valid:
            print(-1)
            exit()
    elif char == 'c':
        for stack in stack_list:
            if stack[-1] == 'a':
                stack.append(char)
                is_valid = True
                break
        if not is_valid:
            print(-1)
            exit()
    elif char == 'k':
        for stack in stack_list:
            if stack[-1] == 'c':
                stack.append(char)
                is_valid = True
                break
        if not is_valid:
            print(-1)
            exit()
answer = 0
for stack in stack_list:
    if len(stack)%5 == 0:
        answer += 1
    else:
        print(-1)
        exit()
print(answer)

