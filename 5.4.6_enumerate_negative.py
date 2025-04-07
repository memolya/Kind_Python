nums = list(map(float, input().split()))

for i, n in enumerate(nums):
    if n < 0:
        nums[i] = -1.0

print(*nums)


