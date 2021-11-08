import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
answer = 0
for _ in range(N):
    st = input()
    done_list = []
    prev = st[0]
    for char in st[1:]:
        if char in done_list:
            answer -= 1
            break
        if char != prev:
            done_list.append(prev)
        prev = char
    answer += 1
print(answer)