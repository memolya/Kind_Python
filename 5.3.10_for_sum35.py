n = int(input())
summed = 0

for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        summed += i
print(summed)