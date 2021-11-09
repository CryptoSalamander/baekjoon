A,B,C,M = map(int, input().split())
tire = 0
answer = 0
if A > M:
    print(answer)
    exit()
for _ in range(24):
    if tire + A <= M:
        answer += B
        tire += A
    else:
        tire -= C

print(answer)