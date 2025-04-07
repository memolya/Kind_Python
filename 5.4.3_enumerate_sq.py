nums = list(map(int, input().split()))

for i, n in enumerate(nums): #индекс, значение = enumerate(объект)
    nums[i] = abs(n)**2

print(*nums)