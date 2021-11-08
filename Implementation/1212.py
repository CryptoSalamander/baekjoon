eight = input()
answer = ""
for char in eight:
    a = int(char)
    tmp = 4
    while(True):
        if a // tmp == 1:
            answer += '1'
            a %= tmp
        else:
            answer += '0'
        if tmp == 1:
            break
        tmp /= 2

if eight == '0':
    print(0)
else:
    print(answer.lstrip('0'))