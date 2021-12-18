import sys,math

def input():
    return sys.stdin.readline().rstrip()

st = input()
cnt = 0
tmp = st[0]
for ch in st:
    if ch != tmp:
        cnt += 1
        tmp = ch
print(math.ceil(cnt/2))