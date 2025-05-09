# nums = list(map(int, input().split()))
#
# for i in range(len(nums)-1):
#     for x in range(i+1, len(nums)):
#         if nums[i] > nums[x]:
#             nums[i], nums[x] = nums[x], nums[i]
#
# print(*nums)

nums = list(map(int, input().split()))

for i in range(len(nums) - 1):
    min_idx = i  # Предполагаем, что текущая позиция содержит минимальный элемент
    for x in range(i + 1, len(nums)):
        if nums[x] < nums[min_idx]:
            min_idx = x  # Нашли индекс нового минимального элемента
    if min_idx != i:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # Делаем ОДНУ замену за проход

print(*nums)
