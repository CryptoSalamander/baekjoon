import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    my_list = []
    ps = input().rstrip()
    for char in ps:
        if char == '(':
            my_list.append('(')
        else:
            if not my_list:
                my_list.append('N')
                break
            my_list.pop()
    if my_list:
        print("NO")
    else:
        print("YES")