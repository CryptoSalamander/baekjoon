import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
switch_status = list(map(int, input().split()))
ST = int(input())

for _ in range(ST):
    gender, val = map(int, input().split())
    if gender == 1:
        for i in range(1, (N // val)+1):
            switch_status[val*i-1] = int(not switch_status[val*i-1])
    elif gender == 2:
        if val == 1:
            switch_status[0] = int(not switch_status[0])
        else:
            for i in range(min(val-1, N-val)+1):
                if switch_status[val+i-1] == switch_status[val-i-1]:
                    if i == 0:
                        switch_status[val-1] = int(not switch_status[val-1])
                    else:
                        switch_status[val-i-1] = int(not switch_status[val-i-1])
                        switch_status[val+i-1] = int(not switch_status[val+i-1])
                else:
                    break
answer = []
for switch in switch_status:
    answer.append(str(switch))
if len(answer) > 20:
    for i in range(len(answer) // 20):
        print(" ".join(answer[20*i:20*i+20]))
    print(" ".join(answer[20*i+20:]))

else:
    print(" ".join(answer))
