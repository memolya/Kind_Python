n = list(map(int, input().split()))
sum = 0

for i in range(len(n)):
    if n[i] % 2 != 0:
        sum += n[i]
print(sum)
