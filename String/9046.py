import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for _ in range(T):
    st = input()
    max = 0
    check = False
    for ch in alpha:
        if st.count(ch) > max:
            max = st.count(ch)
            check = False
            answer = ch
        elif st.count(ch) == max:
            check = True
    if check:
        print('?')
    else:
        print(answer)
