import sys

def input():
    return sys.stdin.readline().rstrip()
while(True):
    try:
        s, t = input().split()
        idx = 0
        is_contain = True
        for char in s:
            if t.find(char) == -1:
                is_contain = False
                break
            else:
                idx = t.find(char)
                t = t[idx+1:]
        if is_contain:
            print("Yes")
        else:
            print("No")
    except Exception as e:
        break
