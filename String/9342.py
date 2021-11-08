import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    st = input()
    a_idx = -1
    f_idx = -1
    c_idx = -1
    for i in range(len(st)):
        if st[i] == 'A':
            a_idx = i
            break
    if a_idx == -1 or a_idx > 1:
        print("Good")
        continue

    for i in range(a_idx,len(st)):
        if st[i] != 'A':
            if st[i] == 'F':
                f_idx = i
                break
            else:
                break
    if f_idx == -1:
        print("Good")
        continue

    for i in range(f_idx,len(st)):
        if st[i] != 'F':
            if st[i] == 'C':
                c_idx = i
                break
            else:
                break
    if c_idx == -1:
        print("Good")
        continue

    if c_idx < len(st)-2:
        print("Good")
        continue

    if c_idx == len(st)-2:
        if st[c_idx+1] not in 'ABCDEF':
            print("Good")
            continue

    print("Infected!")

