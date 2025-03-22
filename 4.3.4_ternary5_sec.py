num = int(input())
rng = list(range(0, 59))

res = (num + 1) if (num in rng) else 0
print(res)