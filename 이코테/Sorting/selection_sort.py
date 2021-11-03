import sys
input = sys.stdin.readline

#N = list(map(int, input().rstrip().split()))
N = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(N)):
    min_index = i
    for j in range(i+1,len(N)):
        if N[j] < N[min_index]:
            min_index = j
    N[i], N[min_index] = N[min_index], N[i]
    print(N)

