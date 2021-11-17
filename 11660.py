import sys
def input():
    return sys.stdin.readline().rstrip()
board = []
N, M = map(int, input().split())
for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(1, len(line)):
        line[i] = line[i-1] + line[i]
    board.append(line)
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    for i in range(x1-1, x2):
        if y1-2 < 0:
            answer += board[i][y2-1]
        else:
            answer += board[i][y2-1] - board[i][y1-2]
    print(answer)


