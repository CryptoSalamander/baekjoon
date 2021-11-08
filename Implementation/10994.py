N = int(input())
size = 4*N-3
board = [[' '] * size for _ in range(size)]

def draw(draw_n, idx):
    if draw_n == 1:
        board[idx][idx] = '*'
        return
    size_ = 4 * draw_n - 3
    for i in range(idx, idx+size_):
        board[idx][i] = '*'
        board[idx+size_-1][i] = '*'

        board[i][idx] = '*'
        board[i][idx+size_-1] = '*'

    return draw(draw_n-1, idx+2)

draw(N,0)

for i in range(size):
    print("".join(board[i]))