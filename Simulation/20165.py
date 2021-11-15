import sys
def input():
    return sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
board = []
is_dead = [[False]*M for _ in range(N)]
ans = 0
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

for _ in range(R):
    attack = input().split()
    attack_x, attack_y = int(attack[0])-1, int(attack[1])-1
    defense_x, defense_y = map(lambda x: int(x)-1, input().split())
    i = 0
    if not is_dead[attack_x][attack_y]:
        ans += 1
        is_dead[attack_x][attack_y] = True
        cnt = board[attack_x][attack_y]-1

        if attack[-1] == 'N':
            while cnt:
                cnt -= 1
                i += 1
                if attack_x - i >= 0 and not is_dead[attack_x - i][attack_y]:
                    ans += 1
                    is_dead[attack_x - i][attack_y] = True
                    cnt = max(cnt, board[attack_x - i][attack_y]-1)
        elif attack[-1] == 'E':
            while cnt:
                cnt -= 1
                i += 1
                if attack_y + i < M and not is_dead[attack_x][attack_y+i]:
                    ans += 1
                    is_dead[attack_x][attack_y+i] = True
                    cnt = max(cnt, board[attack_x][attack_y+i]-1)
        elif attack[-1] == 'S':
            while cnt:
                cnt -= 1
                i += 1
                if attack_x + i < N and not is_dead[attack_x + i][attack_y]:
                    ans += 1
                    is_dead[attack_x + i][attack_y] = True
                    cnt = max(cnt, board[attack_x + i][attack_y]-1)
        elif attack[-1] == 'W':
            while cnt:
                cnt -= 1
                i += 1
                if attack_y - i >= 0 and not is_dead[attack_x][attack_y-i]:
                    ans += 1
                    is_dead[attack_x][attack_y-i] = True
                    cnt = max(cnt, board[attack_x][attack_y-i]-1)
    if is_dead[defense_x][defense_y]:
        is_dead[defense_x][defense_y] = False
print(ans)
for row in range(N):
    for col in range(M):
        if is_dead[row][col] == True:
            print('F', end=' ')
        else:
            print('S', end=' ')
    print("")

