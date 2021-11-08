import sys
def input():
    return sys.stdin.readline().rstrip()

N, M, R = map(int,input().split())
arrays = []
for _ in range(N):
    line = list(map(int,input().split()))
    arrays.append(line)

for _ in range(R):
    for stage in range(min(N,M)//2):
        idx_row = N - 1 - stage * 2
        idx_col = M - 1 - stage * 2

        # 아래
        ori = arrays[stage][stage]
        for i in range(1,idx_row+1):
            tmp = arrays[stage+i][stage]
            arrays[stage+i][stage] = ori
            ori = tmp
        # 오른쪽
        for i in range(1, idx_col+1):
            tmp = arrays[N-stage-1][stage+i]
            arrays[N-stage-1][stage+i] = ori
            ori = tmp
        # 위
        for i in range(1, idx_row+1):
            tmp = arrays[N-1-stage-i][M-1-stage]
            arrays[N-1-stage-i][M-1-stage] = ori
            ori = tmp
        # 왼쪽
        for i in range(1, idx_col+1):
            tmp = arrays[stage][M-1-stage-i]
            arrays[stage][M-1-stage-i] = ori
            ori = tmp

for i in range(N):
    print(*arrays[i])

