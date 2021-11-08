N= int(input())
target = int(input())
snail = [[0]*N for _ in range(N)]
start = N**2
for i in range(N):
    snail[i][0] = start
    start -= 1
moving = N-1
end_point = (N-1,0)
while(moving):
    if moving % 2 == 0:
        for i in range(1, moving+1):
            snail[end_point[0]][end_point[1]+i] = start
            start -= 1
        for j in range(1, moving+1):
            snail[end_point[0]-j][end_point[1]+i] = start
            start -= 1
        end_point = (end_point[0]-j,end_point[1]+i)
    else:
        for i in range(1, moving+1):
            snail[end_point[0]][end_point[1]-i] = start
            start -= 1
        for j in range(1, moving+1):
            snail[end_point[0]+j][end_point[1]-i] = start
            start -= 1
        end_point = (end_point[0]+j,end_point[1]-i)
    moving -= 1
for col in range(N):
    result = []
    for row in range(N):
        if(snail[col][row] == target):
            answer = (col+1, row+1)
        result.append(str(snail[col][row]))
    print(" ".join(result))
print(answer[0], answer[1])