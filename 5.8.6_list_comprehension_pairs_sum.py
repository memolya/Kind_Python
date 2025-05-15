nums_1 = list(map(int, input().split()))
nums_2 = list(map(int, input().split()))

result = [nums_1[n] + nums_2[n] for n in range(len(nums_1))]
print(*result)