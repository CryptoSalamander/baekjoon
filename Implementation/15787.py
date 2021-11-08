import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

lst = [[0]*20 for _ in range(N)]

for _ in range(M):
    input_list = list(map(int, input().split()))

    if input_list[0] == 1:
        lst[input_list[1]-1][input_list[2]-1] = 1

    elif input_list[0] == 2:
        lst[input_list[1]-1][input_list[2]-1] = 0

    elif input_list[0] == 3:
        for i in range(19,0,-1):
            lst[input_list[1]-1][i] = lst[input_list[1]-1][i-1]
        lst[input_list[1]-1][0] = 0
    elif input_list[0] == 4:
        for i in range(0,19):
            lst[input_list[1]-1][i] = lst[input_list[1]-1][i+1]
        lst[input_list[1]-1][19] = 0

sets = set(list(map(tuple, lst)))
print(len(sets))