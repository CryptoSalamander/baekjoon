import sys
def input():
    return sys.stdin.readline().rstrip()
near = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0, 1), (1,-1), (1,0), (1,1)]
N = int(input())
mine = []
board = []
final_answer = []
mine_idx = []
check = False
for row in range(N):
    tmp = input()
    mine.append(tmp)
    for col in range(N):
        if tmp[col] == '*':
            mine_idx.append((row,col))
for row in range(N):
    tmp = input()
    board.append(tmp)
    answer = []
    for col in range(N):
        if tmp[col] == 'x':
            if mine[row][col] == '*':
                answer.append('*')
                check = True
            else:
                cnt = 0
                for dir in near:
                    if 0 <= row+dir[0] < N and 0 <= col+dir[1] < N:
                        if mine[row+dir[0]][col+dir[1]] == '*':
                            cnt += 1
                answer.append(str(cnt))
        else:
            answer.append('.')
    final_answer.append(answer)
if check:
    for idx in mine_idx:
        final_answer[idx[0]][idx[1]] = '*'
for answer in final_answer:
    print("".join(answer))

