nums = list(map(int, input().split()))
nums.append(nums[0] != nums[-1])
print(*nums)

