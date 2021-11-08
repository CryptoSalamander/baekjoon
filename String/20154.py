from collections import deque
st = input()
st = list(st)
is_opened = False
three = "AEFGHKMN"
two = "BDPQRTWXY"
one = "CIJLOSUVZ"
for i in range(len(st)):
    if st[i] in three:
        st[i] = 3
    elif st[i] in two:
        st[i] = 2
    else:
        st[i] = 1
answer = deque(st)

while(answer):
    if len(answer) == 1:
        if answer[0]%2 == 0:
            print("You're the winner?")
            exit()
        else:
            print("I'm a winner!")
            exit()
    a = answer.popleft()
    b = answer.popleft()

    if a+b > 10:
        val = (a+b)%10
    else:
        val = a+b
    answer.appendleft(val)

