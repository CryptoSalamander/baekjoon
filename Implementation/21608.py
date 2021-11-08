import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
classroom = [[0]*N for _ in range(N)]
near = [[-1, 0], [1,0], [0,-1], [0,1]]
favr = dict()
def allocate(student):
    stu_idx = student[0]
    favorite = student[1:]
    candidates = []
    mat = [[0]*N for _ in range(N)]
    empty = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            for dir in near:
                if 0 <= col + dir[0] < N and 0 <= row + dir[1] < N:
                    if classroom[col][row] in favorite:
                        mat[col+dir[0]][row+dir[1]] += 1
                    if classroom[col + dir[0]][row + dir[1]] == 0:
                        empty[col][row] += 1
    for row in range(N):
        for col in range(N):
            if classroom[col][row] == 0:
                candidates.append((mat[col][row], empty[col][row], col, row))
    candidates = sorted(candidates, key= lambda x : (-x[0],-x[1],x[2],x[3]))
    classroom[candidates[0][2]][candidates[0][3]] = stu_idx


for _ in range(N**2):
    tmp = list(map(int, input().split()))
    favr[tmp[0]] = [i for i in tmp[1:]]
    allocate(tmp)
answer = 0
for col in range(N):
    for row in range(N):
        cnt = 0
        for dir in near:
            if 0 <= col + dir[0] < N and 0 <= row + dir[1] < N:
                if classroom[col+dir[0]][row+dir[1]] in favr[classroom[col][row]]:
                    cnt += 1
        if cnt != 0:
            answer += 10**(cnt-1)
print(answer)






