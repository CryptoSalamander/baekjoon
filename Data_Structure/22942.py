import sys
from collections import deque
def input():
    return sys.stdin.readline()

def check(x1,r1,x2,r2):
    # 만약 원이 서로 내부에 있다면, 앞에 애들도 체크해주어야함, 외부에 있다면 어차피 겹칠일 X
    if abs(x2-x1) < abs(r1-r2):
        return 2
    # 원이 접하는 부분이 하나라도 있으면
    elif abs(r1-r2) <= abs(x2-x1) <= r1+r2:
        return 1
    # 두 원이 아예 외부에 있는 관계라면
    else:
        return 0

que = deque()
N = int(input())
for _ in range(N):
   x, r = map(int,input().split())
   que.append((x,r))

# x 좌표 기준으로 정렬
que = sorted(que)

for i in range(N-1):
    # 일단 2개씩 비교하고, 원이 내부에 있는 경우에만  검사
    x,r = que[i]
    x2,r2 = que[i+1]
    tmp = check(x,r,x2,r2)
    if tmp == 1:
        print("NO")
        exit()
    if tmp == 2:
        j = i-1
        for k in range(j, -1, -1):
            x3,r3 = que[k]
            res = check(x2,r2,x3,r3)
            if res == 0:
                break
            elif res == 1:
                print("NO")
                exit()
print("YES")