nums = list(map(float, input().split()))

result = [n for n in nums[::2]]
print(*result)