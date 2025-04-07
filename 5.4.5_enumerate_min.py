nums = list(map(float, input().split()))
min_n = nums[0]

for i, n in enumerate(nums):
    if n <= min_n:
        min_n = n

print(min_n)