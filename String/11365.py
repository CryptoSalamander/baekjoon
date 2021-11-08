import sys
def input():
    return sys.stdin.readline().rstrip()

while(True):
    st = input()
    if st == 'END':
        break
    print(st[::-1])