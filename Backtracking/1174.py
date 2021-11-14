from collections import deque
N = int(input())
answer = deque()
final_answer = deque()
def solve(cnt, prev):
    if answer:
        s = "".join(answer)
        final_answer.append(int(s))
    for i in range(10):
        if i > prev:
            answer.appendleft(str(i))
            solve(cnt, i)
            answer.popleft()
solve(0, -1)
final_answer = sorted(final_answer)
if N > len(final_answer):
    print(-1)
else:
    print(final_answer[N-1])
