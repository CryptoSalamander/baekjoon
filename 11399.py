N = int(input())
nums = sorted(list(map(int, input().split())))

for i in range(1,N):
    nums[i] = nums[i] + nums[i-1]
print(sum(nums))
